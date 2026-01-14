from collections import defaultdict, deque

LAMBDA = "lambda"

class Transducer:
    def __init__(self):
        self.states = set()
        self.start = None
        self.finals = set()
        self.in_alpha = set()
        self.out_alpha = set()
        self.transitions = defaultdict(lambda: defaultdict(list))

    def add_transition(self, q, a, out, p):
        self.states.add(q)
        self.states.add(p)
        self.transitions[q][a].append((p, out))


def parse_transducer(path: str) -> Transducer:
    T = Transducer()

    with open(path, "r", encoding="utf-8") as f:
        raw_lines = f.readlines()

    lines = []
    for ln in raw_lines:
        ln = ln.strip()
        if not ln:
            continue
        if ln.startswith("#"):
            continue
        lines.append(ln)

    for ln in lines:
        if ln.startswith("states:"):
            T.states = set(ln.split(":", 1)[1].split())
        elif ln.startswith("start:"):
            T.start = ln.split(":", 1)[1].strip()
        elif ln.startswith("final:"):
            T.finals = set(ln.split(":", 1)[1].split())
        elif ln.startswith("in:"):
            T.in_alpha = set(ln.split(":", 1)[1].split())
        elif ln.startswith("out:"):
            T.out_alpha = set(ln.split(":", 1)[1].split())

    if T.start is None:
        raise ValueError("Lipseste linia 'start:' în fisier.")

    for ln in lines:
        if any(ln.startswith(h) for h in ("states:", "start:", "final:", "in:", "out:")):
            continue
        parts = ln.split()
        if len(parts) != 4:
            raise ValueError(f"Tranzitie invalida: {ln}")
        q, a, out, p = parts
        T.add_transition(q, a, out, p)

    return T


def simulate_all_outputs(
    T: Transducer,
    w: str,
    max_outputs: int = 10000,
    max_out_len: int = 200,
    max_states: int = 300000
):
    results = set()
    q = deque()
    q.append((T.start, 0, ""))

    visited = set()
    visited.add((T.start, 0, ""))

    processed = 0

    while q:
        state, i, out = q.popleft()
        processed += 1
        if processed > max_states:
            break

        if i == len(w) and state in T.finals:
            results.add(out)
            if len(results) >= max_outputs:
                break

        if len(out) > max_out_len:
            continue

        for (ns, o) in T.transitions[state].get(LAMBDA, []):
            out2 = out if o == LAMBDA else out + o
            if len(out2) <= max_out_len:
                key = (ns, i, out2)
                if key not in visited:
                    visited.add(key)
                    q.append((ns, i, out2))

        if i < len(w):
            a = w[i]
            for (ns, o) in T.transitions[state].get(a, []):
                out2 = out if o == LAMBDA else out + o
                if len(out2) <= max_out_len:
                    key = (ns, i + 1, out2)
                    if key not in visited:
                        visited.add(key)
                        q.append((ns, i + 1, out2))

    return results


def main():
    path = "test.txt"
    T = parse_transducer(path)

    print("\n--- Translator incarcat ---")
    print(f"Start: {T.start}")
    print(f"Final: {sorted(T.finals)}")
    print(f"Nr. stari: {len(T.states)}")
    print("---------------------------\n")

    while True:
        w = input("Scrie /enter pt iesire: ")
        if w == "":
            break

        outs = simulate_all_outputs(T, w)

        if not outs:
            print("NU (0 iesiri)")
        else:
            print(f"DA ({len(outs)} iesiri):")
            for s in sorted(outs):
                print(s if s != "" else LAMBDA)


if __name__ == "__main__":
    main()
