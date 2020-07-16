import cv2

cap = cv2.VideoCapture(0);
four_cc = cv2.VideoWriter_fourcc(*'XVID')
# four_cc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
out = cv2.VideoWriter('output.avi', four_cc, 20.0, (640, 480))
# cap = cv2.VideoCapture('name.avi');

print(cap.isOpened())

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

# while True:
#    ret, frame = cap.read()
#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#    cv2.imshow('Frame', gray)

#   if cv2.waitKey(1) & 0xFF == ord('q'):
#       break