import csv

data = [
(1, 'Lotion', 'Cosmetics'),
(2, 'Lotion', 'Cosmetics'),
(3, 'Lotion', 'Cosmetics'),
(4, 'Lotion', 'Cosmetics'),
(5, 'Lotion', 'Cosmetics'),
(6, 'Samsung', 'Electronics'),
(7, 'Samsung', 'Electronics'),
(8, 'Samsung', 'Electronics'),
(9, 'Samsung', 'Electronics'),
(10, 'Samsung', 'Electronics'),
(11, 'Shampoo', 'Cosmetics'),
(12, 'Shampoo', 'Cosmetics'),
(13, 'Shampoo', 'Cosmetics'),
(14, 'Shampoo', 'Cosmetics'),
(15, 'Shampoo', 'Cosmetics'),
(16, 'iPhone', 'Electronics'),
(17, 'iPhone', 'Electronics'),
(18, 'iPhone', 'Electronics'),
(19, 'iPhone', 'Electronics'),
(20, 'iPhone', 'Electronics'),
(29, 'Soap', 'Detergent'),
(30, 'Soap', 'Detergent'),
(31, 'Soap', 'Detergent'),
(32, 'Soap', 'Detergent'),
(33, 'Soap', 'Detergent'),
(34, 'Phone', 'Electronics'),
(35, 'Phone', 'Electronics'),
(36, 'Phone', 'Electronics'),
(37, 'Phone', 'Electronics'),
(38, 'Phone', 'Electronics'),
(39, 'Make_up', 'Beauty'),
(40, 'Make_up', 'Beauty'),
(41, 'iPhone', 'Electronics'),
(42, 'Make_up', 'Beauty'),
(43, 'Make_up', 'Beauty'),
(44, 'Make_up', 'Beauty'),
(45, 'iPhone', 'Electronics'),
(46, 'iPhone', 'Electronics'),
(47, 'iPhone', 'Electronics'),
]

# create a CSV file and write the data to it
with open('data2.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['product_id', 'product_name','product_type'])
    for row in data:
        writer.writerow(row)