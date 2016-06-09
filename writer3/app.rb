require 'simplernlg'

puts SimpleNLG::NLG.render("mary is happy")

puts SimpleNLG::NLG[subject:%w[Kurt Linda], verb:"invite", object:%w[Jake Roswitha], tense:"past", negation:true]

puts SimplerNLG::NLG.render{
  phrase(
    s:"Igor", 
    v:[ 
      phrase(v:"gain",t:"past",perfect:true, o:"wisdom"),
      phrase(v:pre_mod("teach","now"),progressive:true)
    ], 
    o:"everyone")
}

