from pairLQ import pairLQ
from singleLQs import singleLQs
from singleLQvk0 import singleLQvk0
from singleLQvk1 import singleLQvk1

from hepdata_lib import Submission

sub = Submission()
pairLQ(sub)
singleLQs(sub)
singleLQvk0(sub)
singleLQvk1(sub)
sub.create_files("./output")