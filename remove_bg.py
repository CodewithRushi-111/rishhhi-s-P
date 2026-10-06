from PIL import Image

def remove_black_background(input_path, output_path, tolerance=30):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()
    
    newData = []
    for item in datas:
        # Check if the pixel is close to black
        if item[0] < tolerance and item[1] < tolerance and item[2] < tolerance:
            # Change to transparent
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            
    img.putdata(newData)
    img.save(output_path, "PNG")
    print("Done removing background!")

if __name__ == "__main__":
    remove_black_background("c:/Users/rishi/Desktop/rishhhi/profile1.png", "c:/Users/rishi/Desktop/rishhhi/profile1.png", tolerance=40)
