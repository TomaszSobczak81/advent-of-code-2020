from src.aoc.day00 import Day00


class Day14(Day00):
    def compute_part_one_solution(self, version_identifier: str) -> str:
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        memo = {}

        for line in self.input_data_as_lines(
            self.part_one_identifier, version_identifier
        ):
            if line.startswith("mask"):
                mask = line.split(" = ")[1]
                continue

            addr, data = line.split(" = ")
            data_2_bin = format(int(data), "036b")

            memo[addr] = int(
                "".join(
                    [data_2_bin[i] if mask[i] == "X" else mask[i] for i in range(36)]
                ),
                2,
            )

        return str(sum(memo.values()))

    def compute_part_two_solution(self, version_identifier: str) -> str:
        mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        memo = {}

        for line in self.input_data_as_lines(
            self.part_two_identifier, version_identifier
        ):
            if line.startswith("mask"):
                mask = line.split(" = ")[1]
                continue

            addr, data = line.split(" = ")
            addr_2_bin = format(int(addr[4:-1]), "036b")
            float_bits = []

            for i in range(36):
                match mask[i]:
                    case "1":
                        addr_2_bin = addr_2_bin[:i] + "1" + addr_2_bin[i + 1 :]
                    case "X":
                        float_bits.append(i)

            for i in range(2 ** len(float_bits)):
                floating_addr = addr_2_bin
                for j, f in enumerate(float_bits):
                    floating_addr = (
                        floating_addr[:f]
                        + format(i, f"0{len(float_bits)}b")[j]
                        + floating_addr[f + 1 :]
                    )
                memo[int(floating_addr, 2)] = int(data)

        return str(sum(memo.values()))
