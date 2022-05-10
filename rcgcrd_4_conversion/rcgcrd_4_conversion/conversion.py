# Copyright 2022 Kenji Brameld
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

from construct import Container

from rcgcrd_4.msg import RCGCRD

from rcgcrd_4_conversion.robocup_game_control_return_data import RoboCupGameControlReturnData


def msg_to_data(msg: RCGCRD) -> bytes:
    container = Container(
        playerNum=msg.player_num,
        teamNum=msg.team_num,
        fallen=msg.fallen,
        pose=msg.pose,
        ballAge=msg.ball_age,
        ball=msg.ball
    )
    data = RoboCupGameControlReturnData.build(container)
    return data


def data_to_msg(data: bytes) -> RCGCRD:
    parsed = RoboCupGameControlReturnData.parse(data)
    msg = RCGCRD()
    msg.player_num = parsed.playerNum
    msg.team_num = parsed.teamNum
    msg.fallen = parsed.fallen
    msg.pose = parsed.pose
    msg.ball_age = parsed.ballAge
    msg.ball = parsed.ball
    return msg
