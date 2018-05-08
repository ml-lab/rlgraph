# Copyright 2018 The YARL-Project, All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division

import tensorflow as tf

from yarl.components import LayerComponent


class StatefulLayer(LayerComponent):
    """
    A LayerComponent that adds a state that can be stored and reset and that depends on previous inputs
    to this layer (e.g. like a SequenceLayer).
    It offers the reset method to be overwritten by child methods and the Layer-typical apply method,
    in which the actual computation happens.
    For example: If the input is an image of 84x84px (grayscale), a StatefulLayer could make this image a
    sequence of images, depending on previous inputs to our _computation_apply method.
    """
    def _computation_reset(self):
        """
        Returns:
            An op that resets this processor to some initial state.
            E.g. could be called whenever an episode ends.
            This could be useful if the preprocessor stores certain episode-sequence information
            to do the processing and this information has to be reset after the episode terminates.
        """
        pass  # Not mandatory.

    def _computation_apply(self, *inputs):
        """
        Args:
            inputs (any): The input to be processed.

        Returns:
            The op that processes the input Tensor.
        """
        return inputs

