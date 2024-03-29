(* ::Package:: *)

(* ::Section:: *)
(*Renormalization scheme definitions*)


(* ::Subsection::Closed:: *)
(*Declaring unrenormalized parameters*)


DefineUnrenormalizedParameters[List[args__]]:=DefineUnrenormalizeOne/@{args};


DefineUnrenormalizedParameters[args__]:=DefineUnrenormalizeOne/@{args};


DefineUnrenormalizeOne[exp_]:=Block[{},SchemeRules=Append[SchemeRules,FR$delta[{exp},{}]->0];];


(* ::Subsection::Closed:: *)
(*Defining a dependent renormalisation constant*)


AddRenormalizationCondition[obj_, rule_]:= Block[{}, SchemeRules=Append[SchemeRules,Rule[obj,rule]]];


(* ::Subsection::Closed:: *)
(*Declaring unrenormalized fields*)


DeclareUnrenormalizedFields[List[args__]]:=DeclareUnrenormalizedOneField/@{args};


DeclareUnrenormalizedFields[args__]:=DeclareUnrenormalizedOneField/@{args};


DeclareUnrenormalizedOneField[exp_]:=Block[{},NoRenoFields=Append[NoRenoFields,exp];];


(* ::Subsection::Closed:: *)
(*Removing vanishing internal parameters*)


EnforceZeroParameters[]:=PrePutIndices/@Cases[(Rule[#[[1]],#[[2]]]&/@IParamList)/.ParameterSwitchesAndSwaps[][[3]]/.Rule->myr,myr[_,0]]/.myr->Rule;


(* ::Subsection::Closed:: *)
(*Declaring real renormalization constants*)


RealFieldRenormalization[{fields__}]:= RealFieldRenormalization/@{fields};


RealFieldRenormalization[field_]:=Block[{}, RealRenoFields=Append[RealRenoFields,field]; CnumQ[FR$deltaZ[{field, field},__]]:=False;];


RealFieldRenormalization[fields___]:= RealFieldRenormalization/@{fields};


RealFieldRenormalization[]:= RealFieldRenormalization/@Select[Flatten[ClassMemberList/@PartList[[All,1,2]]],!(GhostFieldQ[#]===True||GoldstoneQ[#]===True)&];


(* ::Subsection::Closed:: *)
(*Removing an internal parameter renormalization constants*)


RemovingInternalCst[param_]:=Block[{},If[FreeQ[InternalRemovalList,param], InternalRemovalList = Append[InternalRemovalList,param]];];


ExecuteRemovingInternalCst[]:= DeleteDuplicates[Flatten[Cases[Global`RenormalizationRules["Internals"][[1]]/.Rule->myr,myr[FR$delta[{PrePutIndices[#]},{}],_]] &/@ InternalRemovalList,1]/.myr->Rule];


(* ::Subsection::Closed:: *)
(*Clearing the rules*)


ClearRenormalizationScheme[]:=Block[{}, 
  If[Length[FR$RmDblExt]===0,FR$RmDblExt={}];
  Block[{}, CnumQ[FR$deltaZ[{#, _},__]]:=True;]&/@RealRenoFields;
  SchemeRules = {}; InternalRemovalList = {}; Global`EnforceZeros = True; RealRenoFields={}; NoRenoFields = {};
  Global`RenormalizationRules["Externals"]={}; Global`RenormalizationRules["Masses"]={}; Global`RenormalizationRules["Internals"]={{},{}};
  Global`RenormalizationRules["Fields"]={}; Global`RenormalizationRules["Tadpoles"]={}; Global`RenormalizationRules["MassShifts"] = {};
];


ClearRenormalizationScheme[];


(* ::Subsection:: *)
(*Enforcing the scheme*)


SchemeDependence[rules_]:=Block[{output=rules/.SchemeRules},
  output=DeleteCases[output,Rule[aa_,aa_]];
  Return[output];
];


SchemeDependenceInternal[{intdefs_, intrules_}]:=Block[{newintdefs, newintrules},
  (* Simplifying the definitions and the rules according to the scheme *)
  newintdefs = If[FreeQ[#[[2]],FR$delta],Rule[#[[1]],Simplify[#[[2]]]],#]&/@SchemeDependence[intdefs];
  newintrules=intrules/.newintdefs;
  newintrules=If[FreeQ[Coefficient[#[[2]],FR$CT],FR$delta],Rule[#[[1]],(#[[2]]/.FR$CT->0)+FR$CT*Simplify[Coefficient[#[[2]],FR$CT]]],#]&/@newintrules;
  newintrules=SchemeDependence[newintrules];
  newintrules=Rule[#[[1]], Collect[#[[2]],{FR$delta[__], FR$deltaZ[__]}]]&/@newintrules;
  newintrules=Rule[#[[1]],#[[1]]+FR$CT*FR$delta[{#[[1]]},{}]]&/@newintrules;
  newintrules = newintrules/.FR$delta[{Conjugate[aaa_]},{}]:>Conjugate[FR$delta[{aaa},{}]]; 
  newintdefs=DeleteCases[newintdefs,Rule[_,0]];
  (* output *)
  Return[{PrePutIndices/@newintdefs,PrePutIndices/@newintrules}];
];


(* ::Section:: *)
(*Misc*)


(* ::Subsection:: *)
(*Version information*)


MoGRe`Version = "1.1";
MoGRe`Date    = "25.10.2019"


(* ::Subsection:: *)
(*Welcome*)


Welcome[]:=Block[{},
  Print["  -- MoGRe: More General Renormalization in FeynRules --"];
  Print["      > Version: " <> MoGRe`Version];
  Print["      > Date: " <> MoGRe`Date];
  Print["  "];
  Print["      > Author: Benjamin Fuks (LPTHE / Sorbonne U.)"];
  Print["      > Contact: fuks@lpthe.jussieu.fr"];
  Print["  "];
  Print["      > Reference: arXiv:1907.04898 [hep-ph]"];
  Print["  "];
];


(* ::Subsection::Closed:: *)
(*Definitions*)


numQ[FR$CT]=True;  CnumQ[FR$CT]=False;


(* ::Subsection:: *)
(*Printing*)


(* ::Text:: *)
(*Set of methods for print statements*)


TimeStamp[method_, msg_,t0_]:= Block[{ti=SessionTime[]},Print[Style[method,Orange,Bold],": ",msg ," done in ", ti-t0," seconds"];Return[ti];];
SubMethodStamp[method_, msg_]:= Print[Style[method,Darker[Green],Bold],": starting ", msg]; 
Error[ msg_]:=Print[Style["  ** Error: ",Darker[Red],Bold], msg];
Warning[ msg_]:=Print[Style["  ** Warning: ",Darker[Purple],Bold], msg];
DebugPrint[msg__]:=If[Global`MoGRe$Debug,Print[msg]];


(* ::Subsection::Closed:: *)
(*Parallelization*)


(* ::Text:: *)
(*Condition for parallelization (expressions longer than 40 terms and kernel availability)*)


DoPara[expr_]:=Global`FR$Parallelize && Length[expr]>40 && $KernelCount>1;


(* ::Text:: *)
(*Options of the method*)


Options[ParaExec]={Opts->MR$Null};


(* ::Text:: *)
(*Main method (two ways, depending whether the method to parallelize has options*)


ParaExec[func_,arg_,OptionsPattern[]]:=Block[{myoptions=OptionValue[Opts],tmpres,inter},

  tmpres=If[myoptions=!=MR$Null,
    (* with options *)
    DistributeDefinitions[myoptions];SetSharedFunction[func];
    Table[inter=arg[[ii]]; ParallelSubmit[{ii,inter},$Output={}; tmpres=func[inter,Sequence@@myoptions]; $Output={OutputStream["stdout",1]}; tmpres],{ii,Length[arg]}],

    (*no options *)
    SetSharedFunction[func];
    Table[inter=arg[[ii]]; ParallelSubmit[{ii,inter},$Output={}; tmpres=func[inter]; $Output={OutputStream["stdout",1]}; tmpres],{ii,Length[arg]}]
  ];

  (* output and exit *)
  tmpres=WaitAll[tmpres];
  Return[tmpres];
];


(* ::Subsection::Closed:: *)
(*Get the class name of a particle*)


ParticleClassName[particle_]:=If[MemberQ[PartList[[All,1,2]],particle], Cases[PartList[[All,1]],{_,particle}][[1,1]],Error["The particle does not exist"];Abort[]];


(* ::Subsection::Closed:: *)
(*Get the index type of the flavor index*)


ParticleClassFlavorType[class_]:=FlavorIndex/.MR$ClassesRules[class];


(* ::Section:: *)
(*Checks*)


(* ::Subsection::Closed:: *)
(*Mixing*)


(* ::Text:: *)
(*Checks whether the mixing pattern is either a boolean, or a list of 2-tuples*)


CheckRenormalizeOptions["Mixing", mixpattern_]:= Block[{},
  If[BooleanQ[mixpattern],Return[]];
  If[Not[ListQ[mixpattern]], Error["The mixing fields must be provided as a list of n-tuples"]; Abort[]];
  If[Not[And@@(ListQ/@mixpattern)], Error["The mixing fields must be provided as a list of n-tuples"]; Abort[]];
  If[Not[And@@((#===1)&/@(Length[Union[#]]&/@Map[Through,Map[MR$QuantumNumbers,#]&/@mixpattern,{2}]))],
     Error["Imposing the one-loop mixing of fields with different quantum numbers"]; Abort[];]
];


(* ::Subsection::Closed:: *)
(*Coupling orders*)


(* ::Text:: *)
(*Checks whether the selected coupling orders are consistent with the QCDOnly option*)


CheckRenormalizeOptions["Couplings",couplingorders_]:=Block[{},
  If[Not[ListQ[couplingorders]],Error["The CouplingOrders option must be a list of coupling orders"]; Abort[]];
  If[Complement[couplingorders,M$InteractionOrderHierarchy[[All,1]]]=!={},Error["At least one unknown CouplingOrder"]; Abort[]];
];


(* ::Subsection::Closed:: *)
(*Vevs*)


VevDeclarations[]:= Block[{},
  If[Not[And@@(!FreeQ[#[[1]]//.MR$Definitions,#[[2]]]&/@M$vevs)], Error["vev declarations (M$vevs) incompatible with (unphysical) field definitions."]; Abort[]];
];


(* ::Section:: *)
(*Formatting the Lagrangian so that it could be processes by the renormalization method*)


(* ::Text:: *)
(*This method flavor-expands the Lagrangian (necessary as some fields of a given class can be massive or massless so that the renormalization is different.*)
(*Next, the 4-scalar interactions are factored out in case they do not need to be renormalized (option to be provided by the user)*)


FormattingLagrangian[lag_,no4S_,cano_]:=Block[{tmplag,lag4S={},l2pt,irules},
  (* init *)
  tmplag=PRIVATE`Listize[lag];

  (* 1. Flavor expansion *)
  tmplag=If[DoPara[tmplag],
    DebugPrint["  ** Expanding indices over ", Global`FR$KernelNumber," cores"];
    ParaExec[ExpandIndices,tmplag,Opts->{FlavorExpand->True}],
    DebugPrint["  ** Expanding indices"];
    Plus@@(ExpandIndices[#,FlavorExpand->True]&/@tmplag)
  ];
  tmplag=PRIVATE`Listize[Plus@@tmplag];
  
  (* 2. Removing 4-scalar interactions *)
  If[no4S,
    DebugPrint["  ** Removing four scalar interactions"];
    lag4S=Select[tmplag,(GetFieldContent[#]/._?ScalarFieldQ -> S)==={S,S,S,S}&];
    tmplag=Complement[tmplag,lag4S];
  ];

  (* Cleaning the two-point/one-point interactions *)
  If[cano,
    DebugPrint["  ** Inserting canonical two point terms..."];
    tmplag= Select[tmplag,Length[GetFieldContent[#]]>2&];
    l2pt = Block[{sym=If[SelfConjugateQ[#],2,1], idx = $IndList[#]/.Index[type_]:>Index[type,Unique[dum]]},
     Which[
      FermionQ[#]===True,I/sym anti[#] . Ga[mu] . del[#,mu]-Mass[#]/sym anti[#] . # ,
      VectorFieldQ[#]===True,GetQuadraticTerms[-1/(2 sym) If[Length[idx]==1,FS[#,mu,nu]FS[anti[#],mu,nu],FS[#,mu,nu,aa]FS[anti[#],mu,nu,aa]] +1/sym Mass[#]^2 anti[#][Sequence@@idx]#[Sequence@@idx]],
      ScalarFieldQ[#]===True,1/sym del[#[Sequence@@idx],mu]del[anti[#][Sequence@@idx],mu]-1/sym Mass[#]^2 anti[#][Sequence@@idx]#[Sequence@@idx]/.fld_[]:>fld
     ]]&/@Flatten[ClassMemberList/@Select[PartList[[All,1,2]],(GhostFieldQ[#]=!=True)&&(GoldstoneQ[#]=!=True)&]];
    l2pt = ExpandIndices[#,FlavorExpand->True]&/@l2pt,
    (* else *)
    irules = DeleteCases[(Rule[#[[1]],#[[2]]]&/@IParamList)/.ParameterSwitchesAndSwaps[][[3]],Rule[_,0]];
    irules = Join[ParameterSwitchesAndSwaps[][[2]],Flatten[irules/.ConditionalExpression[aa_,_]->aa]/.ParameterSwitchesAndSwaps[][[2]]];
    irules=(If[MemberQ[ParameterSwitchesAndSwaps[][[1]][[All,2]],#1],Solve[#1==(#2//.irules),Cases[ParameterSwitchesAndSwaps[][[1]],{_,#1}][[1,1]]][[1,1]],#1->#2]&)@@@irules;
    irules = Rule[#[[1]],#[[2]]//.MR$Definitions]&/@irules;
    irules = Rule[#[[1]],#[[2]]//.irules]&/@irules;
    DebugPrint["  ** Getting the two point terms..."];
    l2pt=Join[DeleteCases[GetQuadraticTerms/@tmplag,0], Select[tmplag,Length[GetFieldContent[#]]===1&]];
    tmplag=Complement[tmplag,PRIVATE`Listize[Plus@@l2pt]];
    l2pt=Simplify/@ (l2pt//.Join[MR$Definitions,Rule[PrePutIndices[#[[1]]],#[[2]]]&/@irules]);
  ];
  
  (* output *)
  Return[{Join[tmplag,l2pt],lag4S}];
];


(* ::Section:: *)
(*Field renormalization*)


(* ::Subsection::Closed:: *)
(*Shortcut to get a field renormalization constant*)


ConstructDeltaZ[fld1_,fld2_,idx_,newidx_,tp___]:= FR$CT*FR$deltaZ[{fld1,fld2},{DeleteCases[Append[Cases[idx,Index[FindClassFlavor[fld1],_]],Index[FindClassFlavor[fld2],newidx]],Index[MR$Null,_]]}, tp];


(* ::Subsection:: *)
(*Main method to get the replacement rule 'bare field => renormalized field'*)


(* ::Text:: *)
(*The method starts by defining a unique sequence of indices that the given field carries.*)
(*Then, all fields with which the given field can mix, at the loop-level, are determined.*)
(*The renormalized field can then be computed, with off-diagonal terms corresponding to the potential mixing pattern.*)
(*The results for the antifeld are then derived, and the replacement rule finally generated.*)


RenormalizeField[field_]:= Block[{FreeIndices,SummedIndices,MixList,rfield=field,result,antiresult,newidx=Unique["idx"],spidx=Index[Spin,Unique["sp"]]},
  (* 1. Indices *)
  FreeIndices=List@@PrePutIndices[field[Sequence@@Table[Unique["idx"],{Length[$IndList[field]]}]]];

  (* 2. Potiential mixing generated at the loop level *)
  If[AntiFieldQ[field]===True,rfield=anti[field]];
  MixList=DeleteCases[PRIVATE`MR$ClassNameList,_?(UnphysicalQ[#]===True&)];
  MixList=DeleteCases[ MixList,_?(DeleteCases[$IndList[#],Index[FindClassFlavor[#]]]=!=DeleteCases[$IndList[rfield],Index[FindClassFlavor[rfield]]]&)];
  MixList=(DeleteCases[ MixList,_?( Through[MR$QuantumNumbers[#]]=!=Through[MR$QuantumNumbers[rfield]]&)]);

  (* 3. Main routine *)
  result=(If[FermionQ[rfield]===True && GhostFieldQ[rfield]=!=True, 
    ConstructDeltaZ[rfield,#, FreeIndices,newidx,"L"]*ProjM[FreeIndices[[1]],spidx] + ConstructDeltaZ[rfield,#,FreeIndices,newidx,"R"] * ProjP[FreeIndices[[1]],spidx],
    ConstructDeltaZ[rfield,#, FreeIndices,newidx]]*
    (#[Sequence@@DeleteCases[$IndList[#]/.(FreeIndices/.Index[aa_,b_]:>Rule[Index[aa],Index[aa,b]])/.{Index[Spin,_]->spidx,Index[FindClassFlavor[#],___]->Index[FindClassFlavor[#],newidx]},Index[MR$Null,_]]]/.#[]->#)
  )&/@MixList;
  result=Expand[(rfield[Sequence@@FreeIndices]/.rfield[]->rfield )+Plus@@result/2];

  (* Majorana *)
  If[FermionQ[rfield]===True && SelfConjugateQ[field], result = Expand[result/.{FR$deltaZ[{aa_,b_}, {{}}, "R"]:>FR$deltaZ[{aa,b}, {{}}, "L"]}]];

  (* 4. Derivation of results for the antifield case *)
  antiresult=result;
  If[AntiFieldQ[field]===True,
    result=result/.{fld_?(FieldQ[#]===True&)->anti[fld],FR$deltaZ[args__]->Conjugate[FR$deltaZ[args]],ProjP[aa_,b_]->ProjM[b,aa],ProjM[aa_,b_]->ProjP[b,aa]};
    result=Refine[result/.FR$deltaZ[{fi_?(AntiFieldQ[#]===True&),gi_?(AntiFieldQ[#]===True&)},bla___]:>FR$deltaZ[{anti[fi],anti[gi]},bla],Assumptions->Element[FR$CT,Reals]],
    (* else *)
    antiresult=result/.{fld_?(FieldQ[#]===True&)->anti[fld],FR$deltaZ[args__]->Conjugate[FR$deltaZ[args]],ProjP[aa_,b_]->ProjM[b,aa],ProjM[aa_,b_]->ProjP[b,aa]};
    antiresult=Refine[antiresult/.FR$deltaZ[{fi_?(AntiFieldQ[#]===True&),gi_?(AntiFieldQ[#]===True&)},bla___]:>FR$deltaZ[{anti[fi],anti[gi]},bla],Assumptions->Element[FR$CT,Reals]]
  ];

  (* 5. Creating elements for the replacement rule *)
  SummedIndices=Union[Flatten[Complement[PRIVATE`ToIndexList[#]/.Index[_,aa_]->aa, FreeIndices/.Index[_,aa_]->aa]&/@List@@result]];
  FreeIndices=#/.Index[aa_,b_]:>Index[aa,MyPattern[b,Blank[]]]&/@FreeIndices;
  rfield=field[Sequence@@FreeIndices]/.aa_?(FieldQ[#]===True&)[]->aa/.MyPattern->Pattern;

  (* 6. Outputting the replacement rule *)
  result=If[field===anti[field], {MyRuleDelayed[rfield,MyModule[SummedIndices,result]]}, {MyRuleDelayed[rfield,MyModule[SummedIndices,result]],MyRuleDelayed[anti[rfield],MyModule[SummedIndices,antiresult]]}];
  Return[result/.{MyRuleDelayed->RuleDelayed,MyModule[{},aaa_]->aaa}/.MyModule->Module];
];


(* ::Subsection:: *)
(*Expansion over flavors*)


(* ::Text:: *)
(*This perform a full flavor expansion in the rules (to get one rule for each flavor) and in the expression (to have no implicit summed flavor index in the rules)*)
(*First, this method checks what is the flavor index of the bare field and makes this expansion.*)
(*Next, it gets the summed flavor indices in the rules, and makes this flavor expasion.*)


FlavorExpFieldReno[field_, rule_]:=Block[{myfield=field,flavtype,flavindex,nflavors,newfields={field},newrules={rule},kill},
  (* we need the field name and not the antifield name *) 
  If[AntiFieldQ[Head[field]], myfield=anti[field]];

  (* treatment of the flavor of the field *)
  If[PRIVATE`FlavoredQ[field],
    (* We get the type of flavor index, its range and the name of the index as it apepars in the replacement rule*)
    flavtype=ParticleClassFlavorType[ParticleClassName[Head[myfield]]];
    flavindex=(Cases[List@@field, Index[flavtype,_]]/.Pattern->mypattern/.mypattern[aa_,_]:>aa)[[1]];
    nflavors = IndexRange[Index[flavtype]][[-1]];
 
   (* from class to classmembers *)
    newfields=Table[ApplyDefinitions[field/.Index[flavtype,_]->Index[flavtype,ii]],{ii,nflavors}]/.fld_?(FieldQ[#]===True&)[]->fld;
    newrules=Table[
      ApplyDefinitions[Refine[rule,Assumptions->Element[FR$CT,Reals]]/.flavindex->Index[flavtype,ii]/.FR$deltaZ[{aa_,b_},{{Index[flavtype,ii],c___}},tp___]:>FR$deltaZ[{ClassMemberList[Head[myfield]][[ii]],b},{{c}},tp]],
    {ii,nflavors}];
    newrules=newrules/.fld_?(FieldQ[#]===True&)[]->fld
  ];

  (* Treating the implicit sums *)
  newrules=newrules/.{
    FR$deltaZ[{aa_, cls_}, {{ix_}},tp___]*fld_[c___, ix_,d___]:>Plus@@Table[ApplyDefinitions[FR$deltaZ[{aa, ClassMemberList[cls][[jj]]}, {{}},tp]*PrePutIndices[fld[c,jj,d]]],{jj,Length[ ClassMemberList[cls]]}]*kill[ix],
    Conjugate[FR$deltaZ[{aa_, cl_}, {{ix_}},tp___]]*fld_[c___, ix_,d___]:>Plus@@Table[ApplyDefinitions[Conjugate[FR$deltaZ[{aa,ClassMemberList[cl][[jj]]},{{}},tp]]*PrePutIndices[fld[c,jj,d]]],{jj,Length[ClassMemberList[cl]]}]*kill[ix]
  }/.fld_?(FieldQ[#]===True&)[]->fld/.kill[Index[_,aaa_]]->kill[aaa]; 
  newrules=newrules/.{mymod[{a1___,ix_,a2___},bla_]:>mymod[{a1,a2},bla]/; Not[FreeQ[bla,kill[ix]]]}//.{kill[_]->1, mymod[{},bla_]->bla};

  (* output *)
  Return[Inner[RuleDelayed,newfields,newrules,List]/.mymod->Module];
];


(* ::Subsection:: *)
(*Field mixing*)


(* ::Text:: *)
(*This method removes potential loop-induced mixings if not needed.*)
(*By default, all potential mixings are kept, except of FieldMixing is set to False or contains a list of 2-tuples representing all fields that can mix*)


TreatFieldMixing[renorule_,mix_]:=Block[{right = (renorule/.Module->mod)[[2]]},

  (* Field mixing is not allowed *)
  If[mix===False,Return[myrd[renorule[[1]],right/.{FR$deltaZ[{aaa_,b_},__]:>0/;aaa=!=b}]/.myrd->RuleDelayed/.mod->Module]];

  (* Field mixing only allowed for specific fields *)
  Return[myrd[renorule[[1]],right/.{FR$deltaZ[{flds__},__]:>0/;(Not[MatchQ[{flds},{aaa_,aaa_}]]&& Not[MemberQ[Sort/@Flatten[Subsets[#,{2}]&/@mix,1],Sort[{flds}]]] )}]/.myrd->RuleDelayed/.mod->Module];

];


(* ::Subsection::Closed:: *)
(*Tadpole renormalization*)


TadpoleShift[vev_,field_]:=Block[{ShiftedField},
  (* Sanity check *)
  If[Not[SelfConjugateQ[field]],Error["All fields getting a vev must be selfconjugate"];Abort[]];

  (* Getting the shift *)
  ShiftedField=Select[Expand[If[Im[Coefficient[field,vev]]===0,(field+HC[field])/.{vev->0},(field-HC[field])/.{vev->0}]],FieldQ[#]===True&];
  CnumQ[FR$deltat[ShiftedField]]=False;
  Return[Rule[ShiftedField,ShiftedField-FR$CT*FR$deltat[ShiftedField]/Mass[ShiftedField]^2]];
];


TadpoleShifts[fields_]:=Block[{RelevantFields = Select[fields,ScalarFieldQ[#]===True&],rules},
  (*Sanity checks *)
  VevDeclarations[];

  (* Getting the field connected with the vevs and creating the rule; filtering all irrelevant fields*)
  rules=TadpoleShift[Sequence@@#]&/@({#[[2]],#[[1]]/.MR$Definitions}&/@M$vevs);
  Return[Select[rules,MemberQ[RelevantFields,#[[1]]]&]];
];


DeltaMShifts[lag_]:=Block[{massterms,shifts,FR$delta2,shiftedlag},
  (* Extracting the mass shift induced by the normalization procedure *)
  massterms =Select[lag,!FreeQ[#,FR$CT]&&FreeQ[#,FR$deltaZ]&& FreeQ[#,_?(GhostFieldQ[#]===True&)]&& FreeQ[#,_?(GoldstoneQ[#]===True&)]&& Length[GetFieldContent[#]]===2&];
  If[massterms==={},massterms={{}}, $Output=OpenWrite[];massterms=(GetMassSpectrum[Plus@@massterms])[[1,2;;,{1,2}]];$Output={OutputStream["stdout",1]}];
  shifts=Flatten[If[FreeQ[#,FR$delta],{},Solve[Simplify[#[[2]]/.{FR$deltat[_]->0,FR$delta->FR$delta2}]==#[[2]],{Cases[#[[2]],_FR$delta,\[Infinity]][[1]]}]/.FR$delta2->FR$delta]&/@massterms];
  
  (* Preparing the replacement rules and applying them *)
  shifts=Join[shifts, (Expand[#/.shifts]&/@Global`RenormalizationRules["Internals"][[1]])];
  shifts=Select[shifts,!MemberQ[Global`RenormalizationRules["Internals"][[1,All,2]],#[[2]]]&];
  shiftedlag =Expand[#/.shifts]&/@lag;

  (* output *)
  Return[{shifts, PRIVATE`Listize[Expand[Plus@@shiftedlag]]}];
];


(* ::Subsection:: *)
(*Wrapper*)


(* ::Text:: *)
(*Loop over all relevant fields; the lagrangian must be properly formatted*)


Renormalization["Fields", lag_, couplingorders_]:= Block[{fields, orderrules,myrule},
  (* Relevant orders *)
  orderrules =myrule[#,1]&/@ Select[M$InteractionOrderHierarchy[[All,1]],Not[MemberQ[couplingorders,#]]&];

  (* Getting the fields involved in the interactions related to the coupling orders under consideration *)
  fields=Select[lag, Union[
    Map[PRIVATE`GetIntOrder,If[ListQ[#],#,{#}]//.{ del[aa_,_]->aa,_?(FieldQ[#]===True&)[__]->1,Dot->Times,Index[_,i_]->i}]/.PRIVATE`GetIntOrder->IntOrder/.(orderrules/.myrule->Rule)]=!={1}&];
  fields=Flatten[GetFieldContent/@fields];
  fields=Union[If[AntiFieldQ[#],anti[#],#]&/@ DeleteCases[fields,_?(UnphysicalQ[#] || GhostFieldQ[#]===True &)]];
  fields = Select[fields,!MemberQ[NoRenoFields,#]&];

  (* Renormalization *)
  fields = Flatten[RenormalizeField /@ fields];

  (* exiting the function *)
  Return[fields];
];


(* ::Section:: *)
(*Parameter renormalization*)


(* ::Subsection:: *)
(*Get replacement rules*)


(* ::Text:: *)
(*This method check whether some external parameters and internal parameters must be traded.  It then gets a formatted list for the switches.*)
(*It also format the parameter names (matrix elements with things as "1x1" for the "1,1" element must be replaced by things like M[1,1])*)


ParameterSwitchesAndSwaps[]:=Block[{switches1,switches2,renames},

  (* Getting and formatting the switches *)
  switches1=DeleteCases[FR$LoopSwitches/.Index[_,b_]->b/.MR$Restrictions,Rule[_,0]];
  switches2=DeleteCases[FR$RmDblExt/.Index[_,b_]->b/.MR$Restrictions,Rule[_,0]];
  renames = Reverse/@DeleteCases[Union[Rule[#[[1]],#[[2]]]&/@PRIVATE`$ParamListtemp],Rule[aa_,aa_]]/.Index[_,b_]->b;

  (* output *)
  Return[{switches1,switches2,renames}];
];


(* ::Subsection:: *)
(*Main method to get the replacement rules 'bare parameter' to 'renormalized parameter'*)


(* ::Text:: *)
(*The method starts by getting all necessary switches (trade-of of external/internal parameters, etc...).*)
(*Then we start the real business:*)
(*   - we get the list of External parameters.*)
(*   - we focus on the internal parameters and deduce the list of those that can appear in the bare Lagrangian*)
(*   - we then get the list of masses to renormalize (removing those of the non QCD fields in the QCD case)*)
(* Finally, we renormalize the external parameters (g -> g + delta g) and deduce the renormalization relations for the internal parameters.*)


Renormalization["Parameters", fields_]:=Block[{switches, Externals,Internals, Masses, IntRules, ZeroRules,simplifs,myRule},
  (* Getting the switches *)
  switches = ParameterSwitchesAndSwaps[]; 

  (* External parameters (without the masses and after applying the switches *)
  Externals=Sort[Flatten[EParamList[[All,2,All,2,1]]]]/.switches[[3]]/.Rule@@@switches[[1]]/.switches[[2]];
  Externals=Select[Externals,Not[MemberQ[MassList[[2,All,2]],#]]&];
  (CnumQ[FR$delta[{#},{}]]=CnumQ[#])&/@Externals;

  (* Internal parameters (applying the switches where relevant) *)
  Internals = If[Global`EnforceZeros,
    DeleteCases[(Rule[#[[1]],#[[2]]]&/@IParamList)/.switches[[3]],Rule[_,0]],
    (Rule[#[[1]],#[[2]]]&/@IParamList)/.switches[[3]]
  ];
  Internals=If[FreeQ[switches[[1,All,2]],#[[1]]],#,Solve[#[[1]]==(#[[2]]//.Internals),Cases[switches[[1]],{_,#[[1]]}][[1,1]] ][[1]]]&/@Internals;
  Internals=Join[switches[[2]],Flatten[Internals/.ConditionalExpression[aa_,_]->aa]/.switches[[2]]];
  Internals = Rule[#[[1]],#[[2]]//.MR$Definitions]&/@Internals;
  Internals = Rule[#[[1]],#[[2]]//.Internals]&/@Internals;

  (* Masses *)
  Masses=DeleteCases[Union[Mass/@fields],0];
  (CnumQ[FR$delta[{#},{}]]=False)&/@Masses;

  (* From bare parameters to renormalized parameters *)
  simplifs=Cases[SchemeRules/.Rule->myRule,myRule[_,0]]/.myRule->Rule;
  Externals=Rule[#,#+FR$CT*FR$delta[{#},{}]]&/@Externals;
  Masses=Rule[#,#+FR$CT*FR$delta[{#},{}]]&/@Masses;
  IntRules =Select[ Internals/.Join[Externals, Masses],Not[FreeQ[#,FR$CT]]&];
  ZeroRules =Rule[FR$delta[{#},{}],0]&/@Select[ Internals/.Join[Externals, Masses],FreeQ[#,FR$CT]&][[All,1]];
  Internals=Flatten[If[CnumQ[#], List[Rule[#,#+FR$CT*FR$delta[{#},{}]],Rule[Conjugate[#],Conjugate[#]+FR$CT*Conjugate[FR$delta[{#},{}]]]],Rule[#,#+FR$CT*FR$delta[{#},{}]]]&/@Internals[[All,1]]];
  Internals=DeleteCases[Internals/.simplifs/.ZeroRules,Rule[aa_,aa_]];
  Internals = Internals/.FR$delta[{Conjugate[aaa_]},{}]:>Conjugate[FR$delta[{aaa},{}]]; 
  IntRules=If[FreeQ[#/.simplifs/.ZeroRules,FR$CT],
    Rule[#[[1]],#[[1]]],
    Rule[#[[1]],Expand[Normal[Series[#[[2]]/.simplifs,{FR$CT,0,1}]]/(Normal[Series[#[[2]],{FR$CT,0,0}]]/#[[1]])]]]&/@IntRules;
  IntRules = Rule[FR$delta[{#[[1]]},{}],Collect [#[[2]]-#[[1]],{ FR$delta[__]},Simplify]]/.FR$CT->1&/@IntRules;
 
  (* Output *)
  Return[{(Externals/.simplifs),(Masses/.simplifs), Internals, IntRules}];
];


(* ::Section:: *)
(*Tools*)


(* ::Subsection::Closed:: *)
(*Get all renormalization constants*)


(* ::Text:: *)
(*Allow to extract all the possible renormalization constants of the *)


ParameterRenormalizationConstants[]:= Block[{RenoPrms,RenoFields,dummy,tmplag},
  {RenoPrms,dummy,dummy,dummy}=Renormalization["Parameters",{}];  
  RenoPrms = DeleteCases[Coefficient[#,FR$CT]&/@RenoPrms[[All,2]],Conjugate[__]];
  RenoPrms = Join[FR$delta[{#},{}]&/@Union[MassList[[2,All,2]]],RenoPrms];
  Return[Union[RenoPrms]];
];


FieldRenormalizationConstants[lag_]:=Block[{dummy = Global`MoGRe$Debug, tmplag, RenoFields},
  (* Verbose = off *)
  Global`MoGRe$Debug=False; 

  (* Lagrangian formatting *)
  tmplag = Expand[lag-(lag/.{(_?FieldQ)[__]->0,_?FieldQ->0})];
  tmplag= FormattingLagrangian[tmplag,False][[1]];

  (* Constants *)
  RenoFields=Flatten[FlavorExpFieldReno[Sequence@@(#/.{Module->mymod})]&/@Renormalization["Fields",tmplag,OptionValue[Global`MoGRe$Renormalize,CouplingOrders]]];
  If[OptionValue[Global`MoGRe$Renormalize,FlavorMixing]=!=True,RenoFields = TreatFieldMixing[#,OptionValue[Global`MoGRe$Renormalize,FlavorMixing]]&/@RenoFields];
  RenoFields=Expand[Coefficient[#,FR$CT]]&/@RenoFields[[All,2]];
  RenoFields=Union[DeleteCases[Select[Expand[#],!FreeQ[#,FR$deltaZ]&]&/@(RenoFields/.Plus->Sequence),Conjugate[_]]];

  (* Output and verbose set to default again *)
  Global`MoGRe$Debug = dummy;
  Return[RenoFields];
];


RenormalizationConstants[lag_]:= InputForm[Join[FieldRenormalizationConstants[lag], ParameterRenormalizationConstants[]]];


(* ::Section:: *)
(*Main method*)


ShiftRules[]:= Block[{irules,rules},
  irules = ExecuteRemovingInternalCst[];
  rules = Join[Global`RenormalizationRules["Externals"],Global`RenormalizationRules["Masses"],Global`RenormalizationRules["Internals"][[2]],Global`RenormalizationRules["Fields"]];
  Return[rules/.irules];
];


Options[Global`MoGRe$Renormalize]={Exclude4Scalars->False,FlavorMixing->True, Global`CouplingOrders->M$InteractionOrderHierarchy[[All,1]], Global`CanonicalTwoPoints -> False};


Global`MoGRe$Renormalize[lag_, OptionsPattern[]]:=Block[{time=SessionTime[],lasttime,tmplag,lag4S, dum1, dum2,ishift,tmpCC},

  (* Initialization *)
  Welcome[];
  If[Global`MoGRe$Debug,SubMethodStamp["Renormalize[]","initialization"]];
  FR$Loop=True;                (*Keep two point in the vertex list*)
  CheckRenormalizeOptions["Mixing",OptionValue[FlavorMixing]];
  CheckRenormalizeOptions["Couplings",OptionValue[CouplingOrders]];
  tmplag = Expand[lag-(lag/.{(_?FieldQ)[__]->0,_?FieldQ->0})];
  If[Global`EnforceZeros, tmplag = tmplag/.EnforceZeroParameters[]];
  If[Global`MoGRe$Debug,lasttime=TimeStamp["Renormalize[]","initialization" ,time]];
  
  (* Formatting the Lagrangian *)
  If[Global`MoGRe$Debug,SubMethodStamp["Renormalize[]","Lagrangian formatting"]];
  {tmplag,lag4S} = FormattingLagrangian[tmplag,OptionValue[Exclude4Scalars],OptionValue[CanonicalTwoPoints]];
  If[Global`MoGRe$Debug,lasttime=TimeStamp["Renormalize[]","Lagrangian formatting" ,lasttime]];
  
  (* Field renormalization *)
  If[Global`MoGRe$Debug,SubMethodStamp["MoGRe$Renormalize[]","field renormalization"]];
  DebugPrint["  ** Getting the replacement rules (bare into renormalized)"];
  Global`RenormalizationRules["Fields"]=Flatten[FlavorExpFieldReno[Sequence@@(#/.{Module->mymod})]&/@Renormalization["Fields",tmplag, OptionValue[CouplingOrders]]];
  If[OptionValue[FlavorMixing]=!=True,
    DebugPrint["  ** Removing unnecessary field mixing"];
    Global`RenormalizationRules["Fields"] = TreatFieldMixing[#,OptionValue[FlavorMixing]]&/@Global`RenormalizationRules["Fields"];
  ];
  DebugPrint["  ** tadpole renormalization"];
  Global`RenormalizationRules["Tadpoles"] = TadpoleShifts[If[Head[#]=!=Symbol, Head[#], #]&/@Global`RenormalizationRules["Fields"][[All,1]]];
  If[Global`MoGRe$Debug,lasttime=TimeStamp["MoGRe$Renormalize[]","field renormalization" ,lasttime]];

  (* Parameter renormalization *)
  If[Global`MoGRe$Debug,SubMethodStamp["MoGRe$Renormalize[]","parameter renormalization"]];
  DebugPrint["  ** Getting the replacement rules (bare into renormalized)"];
  {Global`RenormalizationRules["Externals"],Global`RenormalizationRules["Masses"],dum2,dum1}=Renormalization["Parameters",If[Head[#]=!=Symbol, Head[#], #]&/@Global`RenormalizationRules["Fields"][[All,1]]];
  Global`RenormalizationRules["Internals"]={dum1,dum2};
  DebugPrint["  ** Enforcing the renormalization scheme"];
  Global`RenormalizationRules["Externals"]= SchemeDependence[Global`RenormalizationRules["Externals"]];
  Global`RenormalizationRules["Masses"]   = SchemeDependence[Global`RenormalizationRules["Masses"]];
  Global`RenormalizationRules["Internals"]= SchemeDependenceInternal[Global`RenormalizationRules["Internals"]];
  If[Global`MoGRe$Debug,lasttime=TimeStamp["MoGRe$Renormalize[]","parameter renormalization" ,lasttime]];
   
  (* Lagrangian (with a special treatment for charge-conjugate fields) *)
  If[Global`MoGRe$Debug,SubMethodStamp["MoGRe$Renormalize[]","Lagrangian renormalization"]];
  DebugPrint["  ** Shifting parameters and fields"];
  ishift = ShiftRules[];
  tmplag = (#/.CC[fld_][inds__]:>tmpCC[fld[inds]]/.ishift/.Global`RenormalizationRules["Tadpoles"])&/@tmplag;
  tmplag =Normal[Series[(Expand[#/.tmpCC->CC/.Dot->FR$Dot/.FR$Dot->Dot]),{FR$CT,0,1}]]&/@tmplag;
  tmplag=PRIVATE`Listize[Expand[Plus@@tmplag]];
  DebugPrint["  ** Absorbing all mass shifts in the renormalization constant"];
  {Global`RenormalizationRules["MassShifts"],tmplag}=DeltaMShifts[tmplag];  
  tmplag = Collect[#,{FR$CT},Simplify]&/@tmplag;
  If[Global`MoGRe$Debug,lasttime=TimeStamp["MoGRe$Renormalize[]","Lagrangian renormalization" ,lasttime]];

  (* output *)
  Return[Plus@@Join[tmplag,lag4S]];
];
