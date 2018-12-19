#!/bin/sh
SERVICE='ProjectM'
 
if ! (( ps ax | grep -v grep | grep $SERVICE > /dev/null ))
then
	
	python [path to ProjectM]    

    
fi
