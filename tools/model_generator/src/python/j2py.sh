old_ext=".java"
new_ext=".py"
basejavapath="../com/libiec61850/"
declare -a directories=("tools/" "scl/" "scl/communication/" "scl/types/" "scl/model/")
for dir in "${directories[@]}"
  do
  path=$basejavapath$dir
  rm $dir
  mkdir $dir
  for file in $(ls $path); do
    j2py $path"${file##*/}" > $dir"${file##*/}"
    fp=$dir"${file}"
    newfp="${fp/"$old_ext"/"$new_ext"}"
    echo $newfp
    mv "${fp}" "${newfp}"
  done
done
