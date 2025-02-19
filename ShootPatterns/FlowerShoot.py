from Bullet import Bullet
from ShootPatterns.ShootPattern import ShootPattern
from pygame import sprite
import math

class FlowerShoot(ShootPattern):
    def shoot(self, x: int, y: int, bullet_group: sprite.Group) -> None:
        bullet_pos = self._get_bullet_pos_around(x, y, self.bullet_count, self.spawn_rad)
        angle_step = math.radians(360) / self.bullet_count

        for i in range(len(bullet_pos)):
            angle = angle_step * i
            bullet_group.add(Bullet(bullet_pos[i], angle, delta_curve=0.03))