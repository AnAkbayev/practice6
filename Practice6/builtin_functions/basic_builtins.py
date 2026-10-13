values = [12, 5, 28, 9]

print("len:", len(values))
print("sum:", sum(values))
print("min:", min(values))
print("max:", max(values))
print("sorted:", sorted(values))

value = "42"
print("type before conversion:", type(value))
integer_value = int(value)
float_value = float(value)
string_value = str(integer_value)
print("int conversion:", integer_value, type(integer_value))
print("float conversion:", float_value, type(float_value))
print("str conversion:", string_value, type(string_value))

print("bool(0):", bool(0))
print("bool('hello'):", bool("hello"))
print("list('cat'):", list("cat"))
print("tuple([1, 2]):", tuple([1, 2]))
