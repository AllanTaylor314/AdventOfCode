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

let rec bron_kerbosch r p x =
  if p = StringSet.empty then r
  else
    let v = List.hd (StringSet.to_list p) in
    let rec_candidate =
      bron_kerbosch (StringSet.add v r)
        (StringSet.inter p (Hashtbl.find adjacency_matrix v))
        (StringSet.inter x (Hashtbl.find adjacency_matrix v))
    in
    let loop_candidate =
      bron_kerbosch r (StringSet.remove v p) (StringSet.add v x)
    in
    if
      List.compare_lengths
        (StringSet.to_list rec_candidate)
        (StringSet.to_list loop_candidate)
      = 1
    then rec_candidate
    else loop_candidate

let part2 =
  bron_kerbosch StringSet.empty
    (StringSet.of_seq (Hashtbl.to_seq_keys adjacency_matrix))
    StringSet.empty
  |> StringSet.to_list |> List.sort compare |> String.concat ","

let () = printf "Part 2: %s\n" part2
