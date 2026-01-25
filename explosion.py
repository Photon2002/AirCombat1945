import gameConst

def update_explosions(explosions, frames, now):
    for explosion in explosions[:]:
        if now - explosion["last_update"] >= gameConst.EXPLOSION_FRAME_TIME:
            explosion["last_update"] = now
            explosion["frame"] += 1

            if explosion["frame"] >= len(frames):
                explosions.remove(explosion)

def draw_explosions(screen, explosions, frames):
    for explosion in explosions:
        frame_img = frames[explosion["frame"]]
        rect = frame_img.get_rect(center=explosion["pos"])
        screen.blit(frame_img, rect)