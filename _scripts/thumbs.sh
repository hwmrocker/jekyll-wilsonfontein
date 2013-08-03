cd img/photos
for i in *;do convert -define jpeg:size=200x200 "$i" -thumbnail 140x140^ -gravity center -extent 140x140 "../thumbs/$i"; done
cd -
