#!/bin/bash
#Backout 'N' number of folder when down a rabbit hole

N=$1
P=$PWD
for (( i=1; i<=N; i++ )) do
	P=$P/..
done
echo $P
cd $P
ls
