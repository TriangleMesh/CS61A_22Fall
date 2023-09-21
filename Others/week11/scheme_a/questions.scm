(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15 用递归的思路，因为要track 索引，所以创建helper函数
  ; 错误经验：判断lst是否为nil的条件要放在helper函数里面，不能放在外面（我本来写的是if为nil,return nil,不然（helper s 0），因为递归函数里面需要base case！！！！！
  ; (helper s 0)只是个trigger
  (define (helper lst i)
      (if (eq? lst nil) 
          lst
         (cons (cons i (cons (car lst) nil))
          (helper (cdr lst) (+ i 1)))))
    (helper s 0)) 
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
  (if (or (null? list1) (null? list2)) 
    (append list1 list2)
    (begin (define x (car list1))
    (define y (car list2))
    (if (ordered? x y) (cons x (merge ordered? (cdr list1) list2)) (cons y (merge ordered? list1 (cdr list2)))))
  )) 
  ; END PROBLEM 16

;; Optional Problem 2

;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )
        ((quoted? expr)
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           'replace-this-line
           ; END OPTIONAL PROBLEM 2
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN OPTIONAL PROBLEM 2
           'replace-this-line
           ; END OPTIONAL PROBLEM 2
           ))
        (else
         ; BEGIN OPTIONAL PROBLEM 2
         'replace-this-line
         ; END OPTIONAL PROBLEM 2
         )))

; Some utility functions that you may find useful to implement for let-to-lambda

(define (zip pairs)
  'replace-this-line)
