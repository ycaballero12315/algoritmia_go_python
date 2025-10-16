package algoritmia

import "errors"

type QueueGeneric[T any] struct {
	front *NodeGeneric[T]
	rear  *NodeGeneric[T]
	size  int
}

type NodeGeneric[T any] struct {
	value T
	next  *NodeGeneric[T]
}

func NewQueueGeneric[T any]() *QueueGeneric[T] {
	return &QueueGeneric[T]{}
}

func (q *QueueGeneric[T]) Enqueue(item T) {
	newNode := &NodeGeneric[T]{value: item}

	if q.rear == nil {
		q.front = newNode
		q.rear = newNode
	} else {
		q.rear.next = newNode
		q.rear = newNode
	}

	q.size++
}

func (q *QueueGeneric[T]) Dequeue() (T, error) {
	var zero T

	if q.IsEmpty() {
		return zero, errors.New("queue is empty")
	}

	value := q.front.value
	q.front = q.front.next

	if q.front == nil {
		q.rear = nil
	}

	q.size--
	return value, nil
}

func (q *QueueGeneric[T]) Peek() (T, error) {
	var zero T

	if q.IsEmpty() {
		return zero, errors.New("queue is empty")
	}

	return q.front.value, nil
}

func (q *QueueGeneric[T]) IsEmpty() bool {
	return q.front == nil
}

func (q *QueueGeneric[T]) Size() int {
	return q.size
}
