open Printf

let process_line line =
  String.split_on_char ' ' line
  |> List.filter (fun s -> s <> "")
  |> List.map int_of_string

let rec read_all () =
  match try read_line () |> process_line with _ -> [] with
  | [] -> []
  | a -> a :: read_all ()

let values = read_all ()

let left_list =
  List.sort compare
  @@ List.map (fun pair -> match pair with a :: _ -> a | _ -> 0) values

let right_list =
  List.sort compare
  @@ List.map (fun pair -> match pair with _ :: a :: _ -> a | _ -> 0) values

let part1 left right =
  List.combine left right
  |> List.map (fun p -> abs (fst p - snd p))
  |> List.fold_left ( + ) 0

let () = printf "Part 1: %d\n" (part1 left_list right_list)

let count_occurrence needle haystack =
  List.map (fun item -> if needle = item then 1 else 0) haystack
  |> List.fold_left ( + ) 0

let part2 left right =
  List.map (fun top -> top * count_occurrence top right) left
  |> List.fold_left ( + ) 0

let () = printf "Part 2: %d\n" (part2 left_list right_list)
