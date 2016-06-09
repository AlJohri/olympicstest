require 'simplernlg'

puts SimplerNLG::NLG.render("mary is happy")

puts SimplerNLG::NLG[
	subject:%w[Kurt Linda],
	verb:"invite",
	object:%w[Jake Roswitha],
	tense:"past",
	negation:true]

puts SimplerNLG::NLG.render{
  phrase(
    subject: "Igor",
    verb:[
      phrase(
      	verb:"gain", tense:"past", perfect:true, object:"wisdom"),
      phrase(
      	verb: pre_mod("teach","now"),
      	progressive:true)
    ],
    object:"everyone")}

puts SimplerNLG::NLG.render{
  phrase(
    subject: {noun:"Igor", specifier: "Sweeden"},
    verb:[
      phrase(
      	verb:"gain", tense:"past", perfect:true, object:"wisdom"),
      phrase(
      	verb: pre_mod("teach","now"),
      	progressive:true)
    ],
    object:"everyone")}