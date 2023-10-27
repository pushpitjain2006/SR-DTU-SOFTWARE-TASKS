import cv2

my_image = None
backup_image1 = None
backup_image2 = None
backup_image3 = None


def display_main_menu():
    print("\nMy Image Processing App:")
    print("1. Load an image")
    print("2. Display the image")
    print("3. Save the image")
    print("4. Convert to different color formats")
    print("5. Split image channels (R, G, B)")
    print("6. Remove image background")
    print("7. Apply image blurring")
    print("8. Exit the program")
    print("9. See the previous images in backup")


def image_backup():
    global my_image
    global backup_image1
    global backup_image2
    global backup_image3
    backup_image3 = backup_image2
    backup_image2 = backup_image1
    backup_image1 = my_image


def load_image():
    global my_image
    image_path = input("Enter the path to the image: ")
    image_backup()
    my_image = cv2.imread(image_path)
    if my_image is not None:
        print("Image loaded successfully.")
    else:
        print("Image not found or could not be loaded.")


def display_image():
    global my_image
    if my_image is not None:
        cv2.imshow("My Image", my_image)
        print("Press the space to continue...")
        key = cv2.waitKey(0) & 0xFF
        if key == 32:
            cv2.destroyAllWindows()
    else:
        print("No image to display. Please load an image first.")


def save_processed_image():
    global my_image
    if my_image is not None:
        output_path = input("Enter the path to save the processed image: ")
        cv2.imwrite(output_path, my_image)
        print("Processed image saved successfully.")
    else:
        print("No image to save. Please load an image first.")


def convert_color_format():
    global my_image
    if my_image is not None:
        print("Choose a color format to convert to:")
        print("1. RGB")
        print("2. BGR")
        print("3. HSV")
        print("4. Grayscale")
        __ = int(input("Enter your choice: "))
        image_backup()
        if __ == 1:
            my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2RGB)
        elif __ == 2:
            my_image = cv2.cvtColor(my_image, cv2.COLOR_RGB2BGR)
        elif __ == 3:
            my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2HSV)
        elif __ == 4:
            my_image = cv2.cvtColor(my_image, cv2.COLOR_BGR2GRAY)
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("No image to convert. Please load an image first.")


def split_color_channels():
    global my_image
    if my_image is not None:
        image_backup()
        channels = cv2.split(my_image)
        for i, channel in enumerate(channels):
            cv2.imshow(f"Channel {i}", channel)
        print("Press the space to continue...")
        key = cv2.waitKey(0) & 0xFF
        if key == 32:
            cv2.destroyAllWindows()
    else:
        print("No image to split. Please load an image first.")


def process_background_removal():
    global my_image
    if my_image is not None:
        print("Background removal feature is not yet implemented.")
    else:
        print("No image to process. Please load an image first.")


def apply_image_blur():
    global my_image
    if my_image is not None:
        print("Choose a blur type:")
        print("1. Gaussian Blur")
        print("2. Median Blur")
        print("3. Bilateral Filter")
        _ = int(input("Enter your choice: "))
        image_backup()
        if _ == 1:
            my_image = cv2.GaussianBlur(my_image, (5, 5), 0)
        elif _ == 2:
            my_image = cv2.medianBlur(my_image, 5)
        elif _ == 3:
            my_image = cv2.bilateralFilter(my_image, 9, 75, 75)
        else:
            print("Invalid choice. Please select a valid option.")
    else:
        print("No image to apply blur. Please load an image first.")


def backup_loader():
    if backup_image1 is not None:
        cv2.imshow("backup_image1", backup_image1)
        cv2.waitKey(0)
    if backup_image2 is not None:
        cv2.imshow("backup_image2", backup_image2)
        cv2.waitKey(0)
    if backup_image3 is not None:
        cv2.imshow("backup_image3", backup_image3)
        cv2.waitKey(0)


while True:
    display_main_menu()
    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        load_image()
    elif choice == '2':
        display_image()
    elif choice == '3':
        save_processed_image()
    elif choice == '4':
        convert_color_format()
    elif choice == '5':
        split_color_channels()
    elif choice == '6':
        process_background_removal()
    elif choice == '7':
        apply_image_blur()
    elif choice == '8':
        break
    elif choice == '9':
        backup_loader()
    else:
        print("Invalid choice. Please select a valid option.")

print("Thank you for using My Image Processing App!")
