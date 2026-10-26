#!/usr/bin/env bash
# count_reads.sh — для каждого *.fastq.gz в папке: имя и число ридов
# Использование: ./count_reads.sh <папка>
set -euo pipefail

usage() { echo "Использование: $0 <папка с *.fastq.gz>" >&2; exit 1; }

main() {
  [[ $# -eq 1 ]] || usage
  local dir="$1"
  [[ -d "$dir" ]] || { echo "Нет папки: $dir" >&2; exit 2; }

  shopt -s nullglob                 # если файлов нет — пустой список, а не "*.fastq.gz"
  local files=("$dir"/*.fastq.gz)
  (( ${#files[@]} > 0 )) || { echo "В $dir нет *.fastq.gz" >&2; exit 3; }

  local f lines
  for f in "${files[@]}"; do
    lines=$(zcat -- "$f" | wc -l)
    echo "$(basename "$f" .fastq.gz): $(( lines / 4 ))"
  done
}

main "$@"
