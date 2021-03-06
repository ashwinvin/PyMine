"""Contains packets related to entities."""

from __future__ import annotations

from pymine.types.packet import Packet
from pymine.types.buffer import Buffer

__all__ = ("PlayExplosion",)


class PlayExplosion(Packet):
    """Sent when an explosion occurs (creepers, TNT, and ghast fireballs).                          Each block in Records is set to air. Coordinates for each axis in record is int(X) + record."""

    id = 0x1B
    to = 1

    def __init__(
        self, x: int, y: int, z: int, strength: int, record_count: int, records: list, pmx: int, pmy: int, pmz: int
    ) -> None:
        super().__init__()

        self.x, self.y, self.z = x, y, z
        self.strength = strength
        self.record_count = record_count
        self.records = records
        self.pmx = pmx
        self.pmy = pmy
        self.pmz = pmz

    def encode(self) -> bytes:
        return (
            Buffer.pack("f", self.x)
            + Buffer.pack("f", self.y)
            + Buffer.pack("f", self.z)
            + Buffer.pack("f", self.strength)
            + Buffer.pack("i", self.record_count)
            + Buffer.pack_array("b", self.records)
            + Buffer.pack("f", self.pmx)
            + Buffer.pack("f", self.pmy)
            + Buffer.pack("f", self.pmz)
        )
