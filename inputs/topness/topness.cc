#include "topness.h"
#include <iostream>

using namespace std;

//THIS is the function you want to call to get the variable. Others are helper.
//float topnessMinimization(TLorentzVector met, TLorentzVector lep, TLorentzVector bjet1, TLorentzVector bjet2) {
// Using extern "C" for compiler to not mangle the name of the function
 
double round(double input, int digits){
    return ceil( ( input * pow( 10,digits ) ) - 0.5 ) / pow( 10,digits );
}

extern "C" float topnessMinimization(
  double lep_pt, double lep_eta, double lep_phi, double lep_e,
  double bjet2_pt, double bjet2_eta, double bjet2_phi, double bjet2_e,
  double met_et, double met_phi){
  
  TFitter *minimizer=new TFitter(4) ;
  double p1 = -1;
  minimizer->ExecuteCommand("SET PRINTOUT",&p1,1);
  minimizer->SetFCN(minuitFunctionWrapper);

  //Fill TlorentzVector
  TLorentzVector met;
  met.SetPtEtaPhiE(met_et, 0, met_phi, met_et);
  TLorentzVector lep;
  lep.SetPtEtaPhiE(lep_pt, lep_eta, lep_phi, lep_e);
  TLorentzVector bjet2;
  bjet2.SetPtEtaPhiE(bjet2_pt, bjet2_eta, bjet2_phi, bjet2_e);
 
  // get variables for Topness and use a rounding
 
  int mydigit = 3;
  double iLpx = round(lep.Px(),mydigit);
  double iLpy = round(lep.Py(),mydigit);
  double iLpz = round(lep.Pz(),mydigit);
  double iLpe = round(lep.E(),mydigit);
  double iB2px = round(bjet2.Px(),mydigit);
  double iB2py = round(bjet2.Py(),mydigit);
  double iB2pz = round(bjet2.Pz(),mydigit);
  double iB2pe = round(bjet2.E(),mydigit);
  double iMpx = round(met.Px(),mydigit);
  double iMpy = round(met.Py(),mydigit);
  double iMpz = round(met.Pz(),mydigit);
  double iMpe = round(met.E(),mydigit);

  //cout<<iLpx<<" "<<iLpy<<" "<<iLpz<<" "<<iLpe<<endl;
  //cout<<iB1px<<" "<<iB1py<<" "<<iB1pz<<" "<<iB1pe<<endl;
  //cout<<iB2px<<" "<<iB2py<<" "<<iB2pz<<" "<<iB2pe<<endl;
  //cout<<iMpx<<" "<<iMpy<<" "<<iMpz<<" "<<iMpe<<endl;
  
  // Define parameters [param number, param name, init val, estimated distance to min, bla, bla] // 300,3000,-3000,3000
  minimizer->SetParameter(0,"pwx",0,500,-3000,3000);
  minimizer->SetParameter(1,"pwy",0,500,-3000,3000);
  minimizer->SetParameter(2,"pwz",0,500,-3000,3000);
  minimizer->SetParameter(3,"pnz",0,500,-3000,3000);
  // fixed parameters
  minimizer->SetParameter(4,"plx",iLpx,0,iLpx-0.001,iLpx+0.001);
  minimizer->SetParameter(5,"ply",iLpy,0,iLpy-0.001,iLpy+0.001);
  minimizer->SetParameter(6,"plz",iLpz,0,iLpz-0.001,iLpz+0.001);
  minimizer->SetParameter(7,"ple",iLpe,0,iLpe-0.001,iLpe+0.001);
  minimizer->SetParameter(8,"pb2x",iB2px,0,iB2px-0.001,iB2px+0.001);
  minimizer->SetParameter(9,"pb2y",iB2py,0,iB2py-0.001,iB2py+0.001);
  minimizer->SetParameter(10,"pb2z",iB2pz,0,iB2pz-0.001,iB2pz+0.001);
  minimizer->SetParameter(11,"pb2e",iB2pe,0,iB2pe-0.001,iB2pe+0.001);
  minimizer->SetParameter(12,"pmx",iMpx,0,iMpx-0.001,iMpx+0.001);
  minimizer->SetParameter(13,"pmy",iMpy,0,iMpy-0.001,iMpy+0.001);
  minimizer->SetParameter(14,"pmz",iMpz,0,iMpz-0.001,iMpz+0.001);
  minimizer->SetParameter(15,"pme",iMpe,0,iMpe-0.001,iMpe+0.001);
  minimizer->FixParameter(4);
  minimizer->FixParameter(5);
  minimizer->FixParameter(6);
  minimizer->FixParameter(7);
  minimizer->FixParameter(8);
  minimizer->FixParameter(9);
  minimizer->FixParameter(10);
  minimizer->FixParameter(11);
  minimizer->FixParameter(12);
  minimizer->FixParameter(13);
  minimizer->FixParameter(14);
  minimizer->FixParameter(15);
  // Run the simplex minimizer to get close to the minimum [no good precision, but robust]
  // For signal regions, no difference seen with migrad, but more stable
  minimizer->ExecuteCommand("SIMPLEX",0,0);
  //minimizer->ExecuteCommand("MIGRAD",0,0);
  //Get the best fit values
  double pwx_fit = minimizer->GetParameter(0);
  double pwy_fit = minimizer->GetParameter(1);
  double pwz_fit = minimizer->GetParameter(2);
  double pnz_fit = minimizer->GetParameter(3);
  delete minimizer;
  // get the function value at best fit
  return log(topnessFunction(pwx_fit,pwy_fit,pwz_fit,pnz_fit,
			     iLpx,iLpy,iLpz,iLpe,
			     iB2px,iB2py,iB2pz,iB2pe,
			     iMpx,iMpy,iMpz,iMpe
			     ));

} // ~ end of Topness Minimization()

// full function
double topnessFunction(double pwx_, double pwy_, double pwz_, double pnz_,
                       double plx_, double ply_, double plz_, double ple_,
                       double pb2x_, double pb2y_, double pb2z_, double pb2e_,
                       double pmx_, double pmy_, double pmz_, double pme_) {
  const double mW = 81.;
  const double mT = 172.;
  const double aW = 5.;
  const double aT = 15.;
    
  // construct the lorentz vectors
  TLorentzVector vW; vW.SetPxPyPzE(pwx_,pwy_,pwz_,(sqrt((mW*mW)+(pwx_*pwx_)+(pwy_*pwy_)+(pwz_*pwz_)))) ;
  TLorentzVector vL; vL.SetPxPyPzE(plx_,ply_,plz_,ple_);
  //TLorentzVector vB1; vB1.SetPxPyPzE(pb1x_,pb1y_,pb1z_,pb1e_);
  TLorentzVector vB2; vB2.SetPxPyPzE(pb2x_,pb2y_,pb2z_,pb2e_);
  //TLorentzVector vMET; vMET.SetPxPyPzE(pmx_,pmy_,pmz_,pme_);
  TLorentzVector vN; vN.SetPxPyPzE((pmx_-pwx_),(pmy_-pwy_),pnz_,(sqrt(pow((pmx_-pwx_),2)+pow((pmy_-pwy_),2)+pow(pnz_,2))));
  // construct the w-term (lost)
  //double tWM = ( pow( ((mW*mW) - (vW.M2())),2) ) / (pow(aW,4));//zero by construction
  // construct the w-term (lep)
  double tWL = ( pow( ((mW*mW) - ((vL+vN).M2())),2) ) / (pow(aW,4));
  // construct the tL-term [seen lepton]
  //double tTL = ( pow( ((mT*mT) - ((vL+vB1+vN).M2())),2) ) / (pow(aT,4));
  // construct the tM-term [miss lepton]
  double tTM = ( pow( ((mT*mT) - ((vB2+vW).M2())),2) ) / (pow(aT,4));
  // construct the CM-term
  //double tCM = ( pow( ((4*(mT*mT)) - ((vL+vN+vW+vB1+vB2).M2())),2) ) / (pow(aCM,4));
  // calculate Topness
  double Topness = tWL + tTM;// + tTL + tCM;

  return Topness;
}
