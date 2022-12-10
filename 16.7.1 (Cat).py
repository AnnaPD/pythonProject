from pets_Cat import Cat

# так как на сайте "Дом питомца" только один кот и всего три питомца разного вида, то запишу всех под видом "кот"

cat1 = Cat('Семён', 'мальчик', '2')
cat2 = Cat('Гоша', 'мальчик', '4')
cat3 = Cat('Мухтар', 'мальчик', '0')

print('Все коты на сайте:\n')
print(cat1.getName(), cat1.getGender(), cat1.getAge(), 'года/лет')
print(cat2.getName(), cat2.getGender(), cat2.getAge(), 'года/лет')
print(cat3.getName(), cat3.getGender(), cat3.getAge(), 'года/лет')
