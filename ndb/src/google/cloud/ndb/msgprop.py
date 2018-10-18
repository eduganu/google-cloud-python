# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Define properties for directly strong ProtoRPC messages."""


__all__ = ["EnumProperty", "MessageProperty"]


class EnumProperty:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError


class MessageProperty:
    def __init__(self, *args, **kwargs):
        raise NotImplementedError