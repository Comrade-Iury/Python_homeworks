from PIL import Image, ImageDraw


def picture(file_name, width: int, height: int, sky_color="#87CEEB", ocean_color="#017B92",
            boat_color="#874535", sail_color="#FFFFFF", sun_color="#FFCF40"):
    boat = Image.new("RGB", (width, height), sky_color)
    drawer = ImageDraw.Draw(boat)

    drawer.rectangle(((0, height * 0.8), (width, height)), ocean_color)
    drawer.ellipse(((width * 0.8, -height * 0.2), (width * 1.2, height * 0.2)), sun_color)
    drawer.polygon(((width * 0.25, height * 0.65), (width * 0.3, height * 0.85), (width * 0.7, height * 0.85),
                    (width * 0.75, height * 0.65), (width * 0.51, height * 0.65), (width * 0.51, height * 0.30),
                    (width * 0.49, height * 0.30), (width * 0.49, height * 0.65)),
                   boat_color)
    drawer.polygon(((width * 0.51, height * 0.30), (width * 0.66, height * 0.45), (width * 0.51, height * 0.60)),
                   sail_color)

    boat.save(file_name)

