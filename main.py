import cv2


def scan(image):
    qcd = cv2.QRCodeDetector()
    ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(image)
    if ret_qr:
        for s, p in zip(decoded_info, points):
            if s:
                print(s)
                color = (0, 255, 0)
            else:
                color = (0, 0, 255)
                print("Unreadable")
            image = cv2.polylines(image, [p.astype(int)], True, color, 8)
    else:
        print("No QR code detected")
    return image


def main():
    image_paths = [
        "images/01-Getting-started.png",
        "images/02-Matsawar-3edel-ya3am.png",
        "images/03-Leffy-bina-ya-donya.png",
        "images/04-Black-mirror.png",
        "images/05-Caesar-cipher.png",
        "images/06-Railfence-cipher.png",
        "images/07-THE-MIGHTY-FINGER.png",
        "images/08-Compresso-Espresso.png",
        "images/09-My-phone-fell-while-taking-this-one-...-or-did-it.png",
        "images/10-Gone-With-The-Wind.png",
        "images/11-weewooweewooweewoo.png",
        "images/12-mal7-w-felfel.png",
        "images/13-2el-noor-2ata3.png",
        "images/14-BANANAAA!!!.png",
        "images/15-beast-mode-computer-vision-(this-one-is-from-wikipedia).jpg",
        "images/16-V3-QR-Code...-can-you-do-it.png"
    ]

    while True:
        user_input = input("Enter the number of the image you want to test (1 to 16) or 'q' to quit: ")
        if user_input.lower() == 'q':
            break
        try:
            choice = int(user_input)
            if choice < 1 or choice > 16:
                print("Invalid choice. Please enter a number between 1 and 16.")
                continue
            selected_image_path = image_paths[choice - 1]
            frame = cv2.imread(selected_image_path)
            if frame is None:
                print(f"Failed to read image: {selected_image_path}")
            else:
                frame = scan(frame)
                cv2.imshow('Initial QR Code', frame)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")


if __name__ == "__main__":
    main()
