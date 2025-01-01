open Printf
module StringSet = Set.Make (String)

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
  Hashtbl.add adjacency_matrix key
    (StringSet.add value
       (try Hashtbl.find adjacency_matrix key
        with Not_found -> StringSet.empty))

let () = List.iter (fun p -> add_edge (fst p) (snd p)) edges
let () = List.iter (fun p -> add_edge (snd p) (fst p)) edges

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

let part2 =
  bron_kerbosch StringSet.empty
    (StringSet.of_seq (Hashtbl.to_seq_keys adjacency_matrix))
  |> StringSet.to_list |> String.concat ","

let () = printf "Part 2: %s\n" part2
