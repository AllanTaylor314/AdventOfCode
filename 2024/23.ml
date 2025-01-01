open Printf
module StringSet = Set.Make (String)
module StringSetSet = Set.Make (StringSet)

let process_line line =
  String.split_on_char '-' line |> function
  | [ a; b ] -> (a, b)
  | _ -> invalid_arg (line ^ " is not of the correct form")

let rec read_lines () =
  match try read_line () with _ -> "" with
  | "" -> []
  | a -> process_line a :: read_lines ()

let edges = read_lines ()
let adjacency_matrix = Hashtbl.create 1013

let add_edge key value =
  (match Hashtbl.find_opt adjacency_matrix key with
  | None -> StringSet.empty
  | Some set -> set)
  |> StringSet.add value
  |> Hashtbl.replace adjacency_matrix key

let () =
  List.iter
    (fun p ->
      add_edge (fst p) (snd p);
      add_edge (snd p) (fst p))
    edges

let rec bron_kerbosch r p =
  if StringSet.is_empty p then r
  else
    let v = StringSet.choose p in
    let rec_candidate =
      bron_kerbosch (StringSet.add v r)
        (StringSet.inter p (Hashtbl.find adjacency_matrix v))
    in
    let loop_candidate = bron_kerbosch r (StringSet.remove v p) in
    if StringSet.cardinal rec_candidate > StringSet.cardinal loop_candidate then
      rec_candidate
    else loop_candidate

let create_pairs n =
  Hashtbl.find adjacency_matrix n
  |> StringSet.to_seq
  |> Seq.map (fun v -> (n, v))

let create_triples (a, b) =
  StringSet.inter
    (Hashtbl.find adjacency_matrix a)
    (Hashtbl.find adjacency_matrix b)
  |> StringSet.to_seq
  |> Seq.map (fun v -> StringSet.of_list [ a; b; v ])

let part1 =
  Hashtbl.to_seq_keys adjacency_matrix
  |> Seq.filter (String.starts_with ~prefix:"t")
  |> Seq.concat_map create_pairs
  |> Seq.concat_map create_triples
  |> StringSetSet.of_seq |> StringSetSet.cardinal

let part2 =
  Hashtbl.to_seq_keys adjacency_matrix
  |> StringSet.of_seq
  |> bron_kerbosch StringSet.empty
  |> StringSet.to_list |> String.concat ","

let () = printf "Part 1: %d\nPart 2: %s\n" part1 part2
