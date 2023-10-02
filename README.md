## Тестовое задание для Mindbox (Cтажер-разработчик Python/C# (Data Engineer))
### Task_1 
Написать на Python библиотеку для поставки внешним клиентам, которая умеет вычислять площадь круга по радиусу и треугольника по трем сторонам. 
Дополнительно учесть:
* Юнит-тесты
* Легкость добавления других фигур
* Вычисление площади фигуры без знания типа фигуры в compile-time
* Проверку на то, является ли треугольник прямоугольным.

### Task_2 
* В датафреймах (pyspark.sql.DataFrame) заданы продукты, категории и связь между ними. Одному продукту может соответствовать много категорий, в одной категории может быть много продуктов. 
Пример датафреймов:

``` Python
+---+------------+
| id|product_name|
+---+------------+
|  1|    product1|
|  2|    product2|
|  3|    product3|
|  4|    product4|
+---+------------+

+---+-------------+
| id|category_name|
+---+-------------+
|  1|    category1|
|  2|    category2|
|  3|    category3|
|  4|    category4|
+---+-------------+

+----------+-----------+
|id_product|id_category|
+----------+-----------+
|         1|          1|
|         1|          2|
|         2|          1|
|         4|          3|
|         4|          2|
+----------+-----------+
```
* Написать метод с помощью PySpark, который вернет все продукты с их категориями (датафрейм с набором всех пар «Имя продукта – Имя категории»). В результирующем датафрейме должны также присутствовать продукты, у которых нет категорий.
``` Python
def result(df_p,df_c,df_pc):
  df_rez = ((df_p.join(df_pc, df_p.id == df_pc.id_product, how='left_outer')).join(df_c, df_c.id == df_pc.id_category, how ='left_outer').orderBy('product_name','category_name')).select(col("product_name").alias("Product"), col("category_name").alias("Category"))
  df_rez.show()
  return df_rez

+--------+---------+
| Product| Category|
+--------+---------+
|product1|category1|
|product1|category2|
|product2|category1|
|product3|     null|
|product4|category2|
|product4|category3|
+--------+---------+
```
