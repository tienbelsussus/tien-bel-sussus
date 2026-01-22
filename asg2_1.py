def fish():
    a= float(input("dien chieu dai cua con ca(cm): "))
    length = 42-a
    if a >= 42:
        print("the zander fulfills the size limit")
    else:
        print(F"When the fish was released back into the lake, its length was still {length} short of the allowed limit.")
fish()