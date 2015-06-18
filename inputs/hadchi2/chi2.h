#ifndef Chi2_h
#define Chi2_h

#include <vector>
#include "TFitter.h"
#include "TLorentzVector.h"
#include "Math/LorentzVector.h"

using namespace std;

static const float PDG_TOP_MASS = 173.5;
static const float PDG_W_MASS = 80.385;

typedef ROOT::Math::LorentzVector<ROOT::Math::PxPyPzE4D<float> > LorentzVector;

double fc2 (double c1, double m12, double m22, double m02, bool verbose = false);
double fchi2 (double c1, double pt1, double sigma1, double pt2, double sigma2,
              double m12, double m22, double m02);
void minuitFunction(int&, double* , double &result, double par[], int);
double calculateChi2(vector<LorentzVector>& jets, vector<float>& sigma_jets, vector<bool>& btag);

//double Chi2Interface(int njets, double* jets_pt, double* jets_eta, double* jets_phi, double* jets_E, double* sigma, bool* jets_btag){


extern "C" double Chi2Interface(int njets, double* jets_pt, double* jets_eta, double* jets_phi, double* jets_E, bool* jets_btag);

#endif
