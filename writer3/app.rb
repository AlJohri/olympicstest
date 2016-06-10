require 'simplernlg'
require 'countries'

def player(name, country)
  country = "United States of America" if country == "America"
  nationality = ISO3166::Country.find_country_by_name(country).nationality
  countrys_person = {noun: name, specifier: country}
  person_of_country = {
    noun: {noun: name, pronoun: true},
    prepositional_phrase: {preposition: "of", rest: country}
  }
  nationality_person = {noun: nationality + " " + name}

  # [countrys_person, person_of_country, nationality_person].sample
  person_of_country
end

def medal_result(event, gold_players: [], silver_players: [], bronze_players: [])
  SimplerNLG::NLG.render {
    phrase(
      subject: gold_players,
      verb: "win",
      object: "gold", # the gold medal in the men's taekwondo 80kg
      tense:"past",
      prepositional_phrases: [
        {preposition: "in", rest: event},
        {preposition: "over", rest: silver_players}
      ])}
end

event = "the men's taekwondo 80kg"

players = {
  paige: player("Paige McPherson", "Russia"),
  barbora: player("Barbora Spotakova", "Czech Republic"),
  anthony: player("Anthony Obame", "Gabon"),
  carlo: player("Carlo Molfetta", "Italy"),
}

gold_players = [players[:barbora], players[:paige]]
silver_players = [players[:anthony], players[:carlo]]

output = medal_result(
  "the men's taekwondo 80kg",
  gold_players: gold_players,
  silver_players: silver_players)

puts output

correct_output = "Barbora Spotakova of Czech Republic and Paige McPherson "\
                 "of Russia won gold in the men's taekwondo 80kg over "\
                 "Anthony Obame of Gabon and Carlo Molfetta of Italy."

raise "mismatch" if output != correct_output