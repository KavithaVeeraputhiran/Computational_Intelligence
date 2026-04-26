(defun fact2 ( n ) ;;function for recursive mentod
        ( if ( = n 0 ) 1
                ( * n ( fact2( - n 1 ) ) )
        )
)


O/P:

CL-USER 11 : 3 > (fact2 5)
120

CL-USER 12 : 3 > (fact2 7)
5040


[23bcs011@mepcolinux ex10]$cat Fibonacci
(defun fibo3 (n)
        (cond
                ((= n 0) 0)
                ((= n 1) 1)
                ((> n 1) ( + (fibo3(- n 1)) (fibo3 (- n 2 ))))
                        ;;;Recursive method
        )
)

O/P:

CL-USER 9 : 3 > (fibo3 3)
2

CL-USER 10 : 3 > (fibo3 7)
13
[23bcs011@mepcolinux ex10]$cat Palindrome
(defun palindrom-p (str)
        (equal str (reverse str))
)

O/P:

CL-USER 6 : 3 > (palindrom-p "madam")
T

CL-USER 7 : 3 > (palindrom-p "hello")
NIL

[23bcs011@mepcolinux ex10]$cat Area_of_circle
(defun AreaOfCircle()
        (terpri)        ;terminate printing
        (princ "Enter the readius:")
        (setq radius (read))     ;simple variable assignment stmt of lisp
        (setq area (* 3.1416 radius radius ) )
        (format t "Radius: = ~F~% Area = ~F" radius area )
)


O/P:

CL-USER 8 : 3 > (AreaOfCircle)

Enter the readius:7
Radius: = 7.0
 Area = 153.9384
NIL
