(define (my-filter pred s) 'YOUR-CODE-HERE
(if (null? s)
    s
    (if (pred (car s)) 
        (cons (car s) (my-filter pred (cdr s)))
        (my-filter pred (cdr s))
)))


(define (interleave lst1 lst2) 'YOUR-CODE-HERE
  (if (or (null? lst1) (null? lst2))
    (append lst1 lst2)
    (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))
  )
)

;注意最后cons里需要连接两个值，且不用加（）

(define (accumulate joiner start n term)'YOUR-CODE-HERE
  (if (= n 0)
    start
    (accumulate joiner (joiner start (term n)) (- n 1) term)
  )
)

(define (no-repeats lst)
  (if (null? lst)
    lst
    (cons (car lst) (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) lst))))
  
  
  )

