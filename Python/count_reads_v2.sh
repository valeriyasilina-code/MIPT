#!/usr/bin/env bash

set -euo pipefail

usage() { echo "Использование: $0 <папка> [потоков, по умолчанию 4]" >&2; exit 1; }


count_one() {
  local f="$1" lines
  lines=$(zcat -- "$f" | wc -l)
  printf '%s\t%d\n' "$(basename "$f" .fastq.gz)" $(( lines / 4 ))
}
export -f count_one   

main() {
  [[ $# -ge 1 && $# -le 2 ]] || usage
  local dir="$1" jobs="${2:-4}"
  [[ -d "$dir" ]] || { echo "Нет папки: $dir" >&2; exit 2; }
  [[ "$jobs" =~ ^[1-9][0-9]*$ ]] || { echo "Число потоков должно быть > 0: $jobs" >&2; exit 2; }

  printf 'sample\treads\n'
  if command -v parallel >/dev/null; then
    find "$dir" -maxdepth 1 -name '*.fastq.gz' -print0 \
      | parallel -0 -j "$jobs" count_one {}
  else

    find "$dir" -maxdepth 1 -name '*.fastq.gz' -print0 \
      | xargs -0 -r -P "$jobs" -I{} bash -c 'count_one "$1"' _ {}
  fi | sort -k1,1
}

main "$@"
