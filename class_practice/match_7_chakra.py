try:
    digit = int(input("Enter a chakra number\t"))

    match digit:
        case 1:
            print("\n1st Chakra – The Root Chakra – Muladhara - 4 Lotus petals - Red Colour - Element:Earth - Area:Pelvic - Chant:Lam")
        case 2:
            print("\n2nd Chakra – The Sacral Chakra – Svadhishthana - 6 Lotus petals - Orange Colour - Element:Water - Area:Aortic - Chant:Vam")
        case 3:
            print("\n3rd Chakra – The Solar Plexus Chakra – Manipura - 10 Lotus petals - Yellow Colour - Element:Fire - Area:above the navel,digestive system,Stumack - Chant:Ram")
        case 4:
            print("\n4th Chakra – The Heart Chakra – Anahata - 12 Lotus petals - Green Colour - Element:Air - Area:Surrouding Heart & Cardiac organs - Chant:Yam ")
        case 5:
            print("\n5th Chakra – The Throat Chakra – Vishuddha - 16 Lotus petals(ShodsashDala/KanthPadma) - Aqua-Blue Color - Element:Ether - Area:Throat - Chant:Hum/Ham")
        case 6:
            print("\n6th Chakra – The Third-Eye Chakra – Ajna - 2 Lotus petals with a downward-pointing triangle under a circle - Violet Colour - Element:Light - Area:lower brain, pituitary gland, spine & sixth sense & eyes, ears, nose, pineal glands, and psychic or extrasensory perception - Chant:Aum")
        case 7:
            print("\n7th Chakra – The Crown Chakra – Sahasrara - 1000 Lotus petals - Pinkish-Violet colour - Element:Wisdom - Area:Limbic(top of head) - Chant:Om")
        case _:
            print("\nThis is not regarding a Main 7 Chakra")
except ValueError as v:
    print(v)
except AssertionError as ae:
    print(ae)
except Exception as e:
    print(e)
finally:
    print("\nYou have only 7 main chakra. So, enter accordingly whenever you have opportunity")
