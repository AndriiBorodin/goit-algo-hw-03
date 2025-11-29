import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_snowflake(t, order, size):
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)


def main():
    try:
        level_input = input("Введіть рівень рекурсії: ")
        order = int(level_input)
    except ValueError:
        print("Потрібно ввести ціле число.")
        return

    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха (Рівень {order}) - Крутіть колесо миші для зуму!")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    print("Йде процес малювання? зачекайте...")
    screen.tracer(0, 0)

    draw_snowflake(t, order, 300)

    screen.update()
    print("Готово! Використовуйте колесо миші для зуму та ЛКМ для переміщення.")

    canvas = screen.getcanvas()
    current_scale = 1.0

    def zoom(event):
        nonlocal current_scale
        if event.delta > 0 or event.num == 4:
            scale_factor = 1.1
        else:
            scale_factor = 0.9

        current_scale *= scale_factor
        canvas.scale("all", 0, 0, scale_factor, scale_factor)
        canvas.configure(scrollregion=canvas.bbox("all"))

    last_x, last_y = 0, 0

    def start_pan(event):
        nonlocal last_x, last_y
        last_x, last_y = event.x, event.y

    def pan(event):
        nonlocal last_x, last_y
        dx = event.x - last_x
        dy = event.y - last_y
        canvas.scan_dragto(event.x, event.y, gain=1)
        last_x, last_y = event.x, event.y

    canvas.bind("<MouseWheel>", zoom)
    canvas.bind("<Button-4>", zoom)
    canvas.bind("<Button-5>", zoom)
    canvas.bind("<ButtonPress-1>", start_pan)
    canvas.bind("<B1-Motion>", pan)
    turtle.done()


if __name__ == "__main__":
    main()