#ifndef SimMuon_DTDigitizer_DTDigiSyncFromTable_H
#define SimMuon_DTDigitizer_DTDigiSyncFromTable_H

/** \class DTDigiSyncFromTable
 *  Digi offsets taken from a synchronization table.
 *
 *  $Date: 2005/12/08 11:30:50 $
 *  $Revision: 1.0 $
 *  \author N. Amapane, R. Bellan - INFN Torino
 */

#include "SimMuon/DTDigitizer/interface/DTDigiSyncBase.h"

class DTDetId;
class DTGeomDetUnit;
namespace edm{class ParameterSet;}

class DTDigiSyncFromTable : public DTDigiSyncBase {
public:
  /// Constructor
  DTDigiSyncFromTable(const edm::ParameterSet&);

  /// Destructor
  virtual ~DTDigiSyncFromTable();

  /// Delays to be added to digi times during digitization, in ns.
  double digitizerOffset(const DTDetId * id, const DTGeomDetUnit* layer=0) const;

  /// Offset to obtain "raw" TDCs for the L1 emulator from digis.
  double emulatorOffset(const DTDetId * id) const;

private:
};
#endif

