cd ../img/photos
for i in *;do convert -define jpeg:size=400x400 "$i" -thumbnail 280x280^ -gravity center -extent 280x280 "../bigthumbs/$i"; done
cd -
