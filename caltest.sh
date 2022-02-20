#!/bin/sh

num1=10
num2=5
op=add

if [[ $# != 3 ]]
then 
	echo "Please pass 3 arguments!  Ex=>  $0 5 2 (add/mul/sub/div)"
fi

add() {

sum=`expr $num1 + $num2`
echo $sum

}



sub() 
{
if [[ $num1 > $num2 ]]
then
	sub=`expr $num1 - $num2`
else
	sub=`expr $num2 - $num1`
fi
echo $sub

}


mul() {

	mul=$(($num1*$num2))
echo $mul

}

div() {
if [[ $num2 == 0 ]]
then
	echo "Anything Divided by zero is Zero !!"
else

div=`expr $num1 / $num2`
echo $div
fi

}


if [ $op == "add" ]
then
	echo "Addition is " 
	add
elif [ $op == "sub" ]
then
	echo "Subtraction is"
	sub
elif [ $op == "mul" ]
then
	echo "Multiplication is"
	mul
elif [ $op == "div" ]
then
	echo "Division is "
	div
else
	echo "Please check the input provided !!"

fi


