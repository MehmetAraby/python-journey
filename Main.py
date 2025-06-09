Text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)."

print(f"The Text → {Text}");

print(False) if(type(Text) != str) else print(True);

print(False) if "It" not in Text else print(True);

print(True) if "It" in Text else print(False);

def Typeof(value) :
    if(type(value) == bool) :
        return 'Boolean';
    elif(type(value) == str) :
        return 'String';
    elif(type(value) == float) :
        return 'Float';
    elif(type(value) == int) :
        return 'Integer';
    elif(type(value) == range) :
        return 'Range';

print(Typeof(True));
print(Typeof(False));
print(Typeof(Text));
print(Typeof(1.1));
print(Typeof(1));

people = [
    'Abdul Hamid Hunfrid', 
    'Tashina Artur', 
    'Fikriye Wibowo', 
    'Adamo Constantia', 
    'Mio Adib', 
    'Rina Sango'
];

print(len(people)) # 6


# Loop

for i in range(len(people)) : print(people[i]);


Fruits =  ['Apple', 'Banana', 'Cherry', 'Orange', 'Kiwi', 'Melon', 'Mango'];

print(Fruits[1::5]) # ['Banana', 'Mango']
print(Fruits[1::2]) # ['Banana', 'Orange', 'Melon']
print(Fruits[2::2]) # ['Cherry', 'Kiwi', 'Mango']
print(Fruits[:5]) # ['Apple', 'Banana', 'Cherry', 'Orange', 'Kiwi']
print(Fruits[3:]) # ['Orange', 'Kiwi', 'Melon', 'Mango']

if 'Apple' in Fruits : print('Yep! Apple in the fruits list');

Fruits[3] = 'Blackcurrant';

print(Fruits);
print('Blackcurrant' in Fruits); # True
print('Orange' in Fruits); # False

Fruits[1::5] = ['Blackcurrant', 'Watermelon'];

print(Fruits);

Fruits.append('Starfruit') ## ArrayPrototypePush in JavaScript;

print(Fruits);



people.insert(0 ,'Ema Leili');
print(people);


people.remove('Ema Leili');
print(people);

"""
const Filter = Arr.filter((value: People) => value === 'Apple');

console.log(Filter);
"""


Values = [value for value in people if value != 'Mio Adib'];
print(Values) # ['Abdul Hamid Hunfrid', 'Tashina Artur', 'Fikriye Wibowo', 'Adamo Constantia', 'Rina Sango']


print([values for values in range(1, 101)]);


a = [
    50,
    150,
    100,
    110,
    120,
    510,
    520,
    530,
    540,
    111,
    200
]


Prices = [
    50,
    100,
    150,
    200,
    250,
    300,
    350,
    400,
    450,
    500,
    550
]

print([PRICE for PRICE in a if PRICE <= 200]);
print([PRICE for PRICE in a if PRICE >= 200]);
print([PRICE for PRICE in a if PRICE == 200]);


print([values.upper() for values in people]);


print([value if value != 'Mio Adib' else 'Rina Sango' for value in people]);



Text = """
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
""";

print(Text);



Nickname = "   I AM ARABY       ";
print(Nickname.strip()); # I AM ARABY without spaces

txt = f"The price is {59:.2f} dollars"
print(txt)



# [...Arr, ...Arr2];

Arr = ['Apple', 'Banana', 'Cherry'];
Arr2 = ['Mango', 'Pineapple', 'Papaya']

Arr.extend(Arr2);

print(Arr); # ['Apple', 'Banana', 'Cherry', 'Mango', 'Pineapple', 'Papaya']

Arr.reverse()

print(Arr) # ['Papaya', 'Pineapple', 'Mango', 'Cherry', 'Banana', 'Apple']

Arr.insert(0, 'Banana');

print(Arr.count('Banana')) #1 "How many values ​​have the same result."

Arr.clear()

print(Arr) # Empty Array


