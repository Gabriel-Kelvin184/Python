intro="This is Gabriel Kelvin F (Reg No : 2347222), In the Academic year2023-2024. I have taken the domain of Stock Management."

#word counting
def count_word_frequency(paragraph, target_word):
    words = paragraph.split()
    word_count = 0
    for word in words:
        word = word.strip('.,!?()[]{}"\'')
        if word.lower() == target_word.lower():
            word_count += 1
    return word_count
paragraph = input("enter the paragraph from which you want to find the word count:")
target_word = input("enter the word that you want to count:")
frequency = count_word_frequency(paragraph, target_word)
print(f"The word '{target_word}' appears {frequency} times in the paragraph.")

#To find strint or int (datatype)
num=["0","1","2","3","4","5","6","7","8","9"]
spld_word=intro.split(" ")
for i in spld_word:
    for j in i:
        if j in num:
            if "." in i:
                print(i," is float")
                break
            else:
                print(i,"is int")
                break
        else:
            print(i," : is string")
            break

#character counting
def count_characters(paragraph):
    alphabets = 0
    numerics = 0
    specials = 0

    for char in paragraph:
        if char.isalpha():
            alphabets += 1
        elif char.isnumeric():
            numerics += 1
        else:
            specials += 1

    return alphabets, numerics, specials
paragraph = "This is Gabriel Kelvin F (Reg No : 2347222)"

alphabets, numerics, specials = count_characters(paragraph)

print(f"Alphabets: {alphabets}")
print(f"Numeric characters: {numerics}")
print(f"Special symbols: {specials}")
def set_operations_example():
    mixed_set = {1, 3.14, "python","Hello", True, (1, 2)}
    print("Initial Set:", mixed_set)
    popped_element = mixed_set.pop()
    print("\nElement popped:", popped_element)
    print("Updated Set after pop:", mixed_set)
    mixed_set.clear()
    print("\nSet after clear:", mixed_set)
    mixed_set.add(42)
    mixed_set.add("python")
    mixed_set.add("World")
    mixed_set.add(False)
    mixed_set.add((3, 4))
    mixed_set.update(["Apple", "Banana", "Cherry", "Date", "Elderberry"])  
    
    # Adding string attributes
    print("Set after adding elements:", mixed_set)
    mixed_set.discard("World")
    print("\nSet after discarding 'World':", mixed_set)
    del mixed_set
set_operations_example()


#sorting the set
def set_operations_example():
    string_set = {"Programming", "Technology", "Data Science", "Artificial Intelligence", "Machine Learning"}
    print("Initial Set:", string_set)
    sorted_set = sorted(string_set, reverse=True)
    print("Sorted Set (Descending Order):", sorted_set)
set_operations_example()

#packing and unpacking of tuple
def tuple_operations_example():
    #packing
    programming_languages = ("Python", "Java", "C++", "JavaScript", "Ruby")
    print("Original Tuple:", programming_languages)
    #unpacking
    first_language, second_language, third_language, fourth_language, fifth_language = programming_languages
    print("\nUnpacked Variables:")
    print("First Language:", first_language)
    print("Second Language:", second_language)
    print("Third Language:", third_language)
    print("Fourth Language:", fourth_language)
    print("Fifth Language:", fifth_language)
tuple_operations_example()

dmn_name=("o","n","l","i","n","e","m","o","b","i","l","e","s","t","o","r","e")
count=0
for i in dmn_name:
    if i=="r":
        count=count+1
print("count of r",count)


#tuple slicing

def slicing_and_negative_indexing(domain_name):
    print("Original Domain Name:", domain_name)
    print("\nPositive Slicing:")
    print("1. Slicing from index 3 to 9:", domain_name[3:10])
    print("2. Slicing from index 0 to 7:", domain_name[:8])
    print("3. Slicing from index 5 to the end:", domain_name[5:])
    print("4. Slicing from index 2 to 11 with step 2:", domain_name[2:12:2])
    print("\nNegative Slicing:")
    print("1. Slicing from the end -8 to the end -3:", domain_name[-8:-2])
    print("2. Slicing from the end -11 to the end -1 with step 2:", domain_name[-11:-1:2])
    print("\nNegative Indexing:")
    print("Last character:", domain_name[-1])
    print("Second to last character:", domain_name[-2])
domain_name = "Online Mobile Store"
slicing_and_negative_indexing(domain_name)
