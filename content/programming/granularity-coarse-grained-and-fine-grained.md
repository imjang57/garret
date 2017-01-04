Title: Granularity (Coarse-grained V.S. Fine-grained)
Date: 2017-01-04
Modified: 2017-01-04
Tags: granularity, coarse-grained, fine-grained, programming
Slug: granularity-coarse-grained-and-fine-grained
Authors: imjang57
Summary: Granularity (Coarse-grained V.S. Fine-grained) 의 의미

# Coarse-grained V.S. Fine-grained in Spark

Coarse-grained 와 Fine-grained 는 한국말로 번역하기가 참 애매한 단어이다. 그래서 의미도 잘 와닿지 않는다.

Quora 에 누군가가 [Spark RDD 에서 사용되는 Coarse-grained 의 개념에 대해 질문](https://www.quora.com/What-does-coarse-grained-mean-in-Spark-RDD)하였는데, 누군가가 coarse-grained 에 대해 아래와 같이 설명한다.:

> Basically, it means that you can write you transformations to be applied to the while dataset, but not individual elements on the dataset. Operations like map, filter, group reduce, but not get(index) or set(index).

> By restricting RDD operations to coarse-grained immutable transformations, Spark is able to provide powerful distributed data processing, while keeping the system fairly simple to understand and operate.

Coarse-grained 와 Fine-grained 는 원래 곡식을 낟알로 만들 때 대충 작업하여 낟알을 거칠하는 것과 세심하게 하여 낟알을 부드럽게 하는 것을 의미한다. 소프트웨어 공학에서 Coarse-grained 와 Fine-grained 는 어떤 작업(Process, Wordload)의 분할 단위가 큰가 작은가를 구분하는 상대적인 의미로 사용된다.

얼마나 세분화 되었는가? 모듈화 되었는가? 한국말로 표현하기가 좀 애매한데, 여튼 어느 정도 grain 되었는지를 나타내는 것을 granularity 라고 한다. 이 [Granularity](https://en.wikipedia.org/wiki/Granularity)에 대한 위키피디아 페이지에 다음과 같은 언급이 있다.:

> Coarse-grained materials or systems have fewer, larger discrete components than fine-grained materials or systems.

> The concepts granularity, coarseness, and fineness are relative, used when comparing systems or descriptions of systems.

