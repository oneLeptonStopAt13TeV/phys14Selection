#include "TFitter.h"
#include "TMath.h"
#include <vector>
#include "Math/LorentzVector.h"
#include <math.h>
#include "TLorentzVector.h"

using namespace std;


//extern "C" float topnessMinimization(TLorentzVector met, TLorentzVector lep, TLorentzVector bjet1, TLorentzVector bjet2, int version=1);

/*
extern "C" float topnessMinimization( TLorentzVecto
  double lep_pt, double lep_eta, double lep_phi, double lep_e,
  double bjet1_pt, double bjet1_eta, double bjet1_phi, double bjet1_e,
  double bjet2_pt, double bjet2_eta, double bjet2_phi, double bjet2_e,
  double met, double met_phi);
*/
double topnessFunction(double pwx_, double pwy_, double pwz_, double pnz_,
                       double plx_, double ply_, double plz_, double ple_,
                       double pb2x_, double pb2y_, double pb2z_, double pb2e_,
                       double pmx_, double pmy_, double pmz_, double pme_);

void minuitFunctionWrapper(int& nDim, double* gout, double& result, double* par, int flg) {
  result = topnessFunction(par[0],par[1],par[2],par[3],
                           par[4],par[5],par[6],par[7],
                           par[8],par[9],par[10],par[11],
                           par[12],par[13],par[14],par[15]
                           );
}
