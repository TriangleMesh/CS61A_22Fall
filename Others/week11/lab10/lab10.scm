(define (over-or-under num1 num2) 'YOUR-CODE-HERE
    (cond
        ((< num1 num2) -1)
        ((= num1 num2) 0)
        (else 1)
            )
    )

(define (make-adder num) 'YOUR-CODE-HERE
    (lambda (inc) (+ num inc))
    )


(define (composed f g) 'YOUR-CODE-HERE
    (lambda (x) (f (g x)))
    )

(define lst 
    (list (cons 1 nil) 2 (cons 3 (cons 4 nil)) 5))


(define (duplicate lst) 'YOUR-CODE-HERE
    (if (null? lst) 
        nil
        (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
    
    ))

