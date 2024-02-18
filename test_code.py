# test_max_pairwise_product.py

import pytest

list_input = [1000000, 90000000]

@pytest.mark.benchmark(group='max_pairwise_product')
def test_max_pairwise_product(benchmark):
    def code_to_benchmark():
        def max_pairwise_product(list):
            first = max_1(list)
            second = max_2(first, list)
            return first, second
    
        def max_1(list):
            max_1 = 0
            for i in list:
                if i > max_1:
                    max_1 = i
            return max_1
    
        def max_2(max_1, list):
            max_2 = 0
            for i in list:
                if i != max_1 and i > max_2:
                    max_2 = i
            return max_2
    
        a, b = max_pairwise_product(list_input)
        result = a * b
    
    # Benchmark the code
    result = benchmark(code_to_benchmark)
    assert result
