        

class Variables() :

    def computeVariables(event) :
        event.MT = computeMT(event)

    # ########
    # #  MT  # 
    # ########

    def computeMT(event) :
        
        leadingLeptonPt = event.selectedLepton[0].Pt
        deltaPhi = event.selectedLepton[0].phi - event.met_phi
        
        MT = sqrt(2 * leadingLeptonPt * event.met * (1 - cos(deltaPhi) ))
        
        return MT
