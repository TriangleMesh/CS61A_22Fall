(define (cddr s) 
    (cdr (cdr s)))

(define (cadr s) 
    (car (cdr s)))
    

(define (caddr s) 'YOUR-CODE-HERE
    (car (cdr (cdr s)))
    )

(define (ascending? asc-lst) 'YOUR-CODE-HERE
    (cond 
          ((or (null? (cdr asc-lst)) (null? asc-lst)) #t)
          ((> (car asc-lst) (cadr asc-lst)) #f)
          (else (ascending? (cdr asc-lst)))
    ))


(define (square n) (* n n))


(define (pow base exp) 'YOUR-CODE-HERE
    (cond 
         ((zero? exp) 1)
         ((= base 1) 1)
         ((even? exp) (square (pow base (/ exp 2))))
         ((odd? exp) (* base (pow base (- exp 1))))
    )
)
