sample_dict = {
    "a": "dog",
    "b": "dog"
}

print(sample_dict)
value = sample_dict.get("dog")
print(value)

value = [key for key in sample_dict if sample_dict[key] == "dog"]
print(value)
