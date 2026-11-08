#! /bin/sh

curl "https://api.hh.ru/vacancies?text=data%20scientist&per_page=20" > hh.json

echo "cool"

read -p "press enter to close..."